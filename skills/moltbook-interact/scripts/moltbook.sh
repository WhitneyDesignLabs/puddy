#!/usr/bin/env bash
# Moltbook CLI helper - Fixed API field names

CONFIG_FILE="${HOME}/.config/moltbook/credentials.json"
OPENCLAW_AUTH="${HOME}/.openclaw/auth-profiles.json"
API_BASE="https://www.moltbook.com/api/v1"

# Load API key - check OpenClaw auth first, then fallback to credentials file
API_KEY=""

# Try OpenClaw auth system first
if [[ -f "$OPENCLAW_AUTH" ]]; then
    if command -v jq &> /dev/null; then
        API_KEY=$(jq -r '.moltbook.api_key // empty' "$OPENCLAW_AUTH" 2>/dev/null)
    fi
fi

# Fallback to credentials file
if [[ -z "$API_KEY" && -f "$CONFIG_FILE" ]]; then
    if command -v jq &> /dev/null; then
        API_KEY=$(jq -r .api_key "$CONFIG_FILE")
    else
        API_KEY=$(grep '"api_key"' "$CONFIG_FILE" | sed 's/.*"api_key"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/')
    fi
fi

if [[ -z "$API_KEY" || "$API_KEY" == "null" ]]; then
    echo "Error: Moltbook credentials not found"
    echo "Create: ~/.config/moltbook/credentials.json"
    exit 1
fi

# Helper function for API calls
api_call() {
    local method=$1
    local endpoint=$2
    local data=$3
    
    if [[ -n "$data" ]]; then
        curl -s -X "$method" "${API_BASE}${endpoint}" \
            -H "Authorization: Bearer ${API_KEY}" \
            -H "Content-Type: application/json" \
            -d "$data"
    else
        curl -s -X "$method" "${API_BASE}${endpoint}" \
            -H "Authorization: Bearer ${API_KEY}" \
            -H "Content-Type: application/json"
    fi
}

case "${1:-}" in
    hot)
        limit="${2:-10}"
        api_call GET "/posts?sort=hot&limit=${limit}"
        ;;
    new)
        limit="${2:-10}"
        api_call GET "/posts?sort=new&limit=${limit}"
        ;;
    post)
        post_id="$2"
        if [[ -z "$post_id" ]]; then
            echo "Usage: moltbook.sh post POST_ID"
            exit 1
        fi
        api_call GET "/posts/${post_id}"
        ;;
    reply)
        post_id="$2"
        content="$3"
        if [[ -z "$post_id" || -z "$content" ]]; then
            echo "Usage: moltbook.sh reply POST_ID CONTENT"
            exit 1
        fi
        api_call POST "/posts/${post_id}/comments" "{\"content\":\"${content}\"}"
        ;;
    create)
        title="$2"
        body="$3"
        submolt="${4:-general}"
        if [[ -z "$title" ]]; then
            echo "Usage: moltbook.sh create TITLE [BODY] [SUBMOLT]"
            echo "Default submolt: general"
            exit 1
        fi
        # If no body provided, use title as both
        if [[ -z "$body" ]]; then
            body="$title"
        fi
        # API expects: submolt (name), title, content
        api_call POST "/posts" "{\"submolt\":\"${submolt}\",\"title\":\"${title}\",\"content\":\"${body}\"}"
        ;;
    test)
        echo "Testing Moltbook API connection..."
        result=$(api_call GET "/posts?sort=hot&limit=1")
        if echo "$result" | grep -q '"success":true'; then
            echo "✅ API connection successful"
            exit 0
        else
            echo "❌ API connection failed"
            echo "$result"
            exit 1
        fi
        ;;
    *)
        echo "Moltbook CLI"
        echo ""
        echo "Commands:"
        echo "  hot [limit]                    Get hot posts"
        echo "  new [limit]                    Get new posts"
        echo "  post ID                        Get specific post"
        echo "  reply POST_ID TEXT             Reply to a post"
        echo "  create TITLE [BODY] [SUBMOLT]  Create new post (default submolt: general)"
        echo "  test                           Test API connection"
        ;;
esac

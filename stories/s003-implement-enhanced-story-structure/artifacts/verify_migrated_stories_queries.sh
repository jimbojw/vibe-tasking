#!/bin/bash
# Copyright 2025 Google LLC 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Determine the script's own directory to construct relative paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
STORIES_DIR="$SCRIPT_DIR/../../" # Root of the stories directory (docs/stories/)

# Define output file paths within the s003 artifacts directory
OUTPUT_S001_STATUS_FILE="$SCRIPT_DIR/s001_status_query_result.txt"
OUTPUT_S002_PRIORITY_FILE="$SCRIPT_DIR/s002_priority_query_result.txt"
OUTPUT_S003_TAG_FILE="$SCRIPT_DIR/s003_tag_query_result.txt"

# --- Test Commands for Migrated Stories ---

# Test s001 by its status ("Done")
echo "Querying s001 by status 'Done'..."
TARGET_S001_FILE="$STORIES_DIR/s001-initial-project-setup/story.md"
if [ -f "$TARGET_S001_FILE" ]; then
  grep -l -E '^status: "Done"' "$TARGET_S001_FILE" | sed -E 's|.*/(s[0-9]+-[^/]+)/story.md$|\1|' > "$OUTPUT_S001_STATUS_FILE"
  echo "s001 status query output saved to $OUTPUT_S001_STATUS_FILE"
else
  echo "ERROR: Target story file not found at $TARGET_S001_FILE" > "$OUTPUT_S001_STATUS_FILE"
fi

# Test s002 by its priority ("High")
echo "Querying s002 by priority 'High'..."
TARGET_S002_FILE="$STORIES_DIR/s002-design-enhanced-story-structure/story.md"
if [ -f "$TARGET_S002_FILE" ]; then
  grep -l -E '^priority: "High"' "$TARGET_S002_FILE" | sed -E 's|.*/(s[0-9]+-[^/]+)/story.md$|\1|' > "$OUTPUT_S002_PRIORITY_FILE"
  echo "s002 priority query output saved to $OUTPUT_S002_PRIORITY_FILE"
else
  echo "ERROR: Target story file not found at $TARGET_S002_FILE" > "$OUTPUT_S002_PRIORITY_FILE"
fi

# Test s003 by one of its tags ("implementation")
echo "Querying s003 by tag 'implementation'..."
TARGET_S003_FILE="$STORIES_DIR/s003-implement-enhanced-story-structure/story.md"
if [ -f "$TARGET_S003_FILE" ]; then
  grep -l -E '^tags: "([^"]*;)*implementation([^"]*;|")[^"]*"' "$TARGET_S003_FILE" | sed -E 's|.*/(s[0-9]+-[^/]+)/story.md$|\1|' > "$OUTPUT_S003_TAG_FILE"
  echo "s003 tag query output saved to $OUTPUT_S003_TAG_FILE"
else
  echo "ERROR: Target story file not found at $TARGET_S003_FILE" > "$OUTPUT_S003_TAG_FILE"
fi

echo "All migrated story query tests complete."

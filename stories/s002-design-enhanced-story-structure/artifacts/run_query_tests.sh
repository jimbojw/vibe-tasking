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

# Determine the script's own directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Define the path to the example story file relative to the script's directory
TARGET_STORY_FILE="$SCRIPT_DIR/example-story-for-testing/story.md"

# Define output file paths
OUTPUT_STATUS_FILE="$SCRIPT_DIR/status_query_result.txt"
OUTPUT_PRIORITY_FILE="$SCRIPT_DIR/priority_query_result.txt"
OUTPUT_TAG_FILE="$SCRIPT_DIR/tag_query_result.txt"

# --- Test Commands ---

# 1. Test Querying by Status ("In Progress")
echo "Running status query..."
if [ -f "$TARGET_STORY_FILE" ]; then
  grep -l -E '^status: "In Progress"' "$TARGET_STORY_FILE" | sed -E 's|.*/([^/]+)/story.md$|\1|' > "$OUTPUT_STATUS_FILE"
  echo "Status query output saved to $OUTPUT_STATUS_FILE"
else
  echo "ERROR: Target story file not found at $TARGET_STORY_FILE" > "$OUTPUT_STATUS_FILE"
fi

# 2. Test Querying by Priority ("High")
echo "Running priority query..."
if [ -f "$TARGET_STORY_FILE" ]; then
  grep -l -E '^priority: "High"' "$TARGET_STORY_FILE" | sed -E 's|.*/([^/]+)/story.md$|\1|' > "$OUTPUT_PRIORITY_FILE"
  echo "Priority query output saved to $OUTPUT_PRIORITY_FILE"
else
  echo "ERROR: Target story file not found at $TARGET_STORY_FILE" > "$OUTPUT_PRIORITY_FILE"
fi

# 3. Test Querying by Tag ("test")
echo "Running tag query..."
if [ -f "$TARGET_STORY_FILE" ]; then
  grep -l -E '^tags: "([^"]*;)*test([^"]*;|")[^"]*"' "$TARGET_STORY_FILE" | sed -E 's|.*/([^/]+)/story.md$|\1|' > "$OUTPUT_TAG_FILE"
  echo "Tag query output saved to $OUTPUT_TAG_FILE"
else
  echo "ERROR: Target story file not found at $TARGET_STORY_FILE" > "$OUTPUT_TAG_FILE"
fi

echo "All tests complete."

export interface CommitMarkers {
  excluded: boolean;
  feature: boolean;
  module: boolean;
  bugfix: boolean;
  docs: boolean;
  refactor: boolean;
}

const MARKER_PATTERNS: Record<keyof Omit<CommitMarkers, "excluded">, RegExp> = {
  feature: /\[x\]\s*added a new feature/i,
  module: /\[x\]\s*added a new module/i,
  bugfix: /\[x\]\s*fixed a bug/i,
  docs: /\[x\]\s*improved documentation/i,
  refactor: /\[x\]\s*refactored old code/i,
};

const EXCLUDE_PATTERN = /\[x\]\s*don'?t include this commit in contributor quest stats/i;

/**
 * Reads the opt-in checklist from `.gitmessage` (see that file) out of a commit's full message.
 * A line only counts once a contributor has uncommented it — git strips '#'-prefixed lines from
 * the final commit message on save, so anything still commented out never reaches this parser.
 */
export function parseCommitMarkers(message: string): CommitMarkers {
  return {
    excluded: EXCLUDE_PATTERN.test(message),
    feature: MARKER_PATTERNS.feature.test(message),
    module: MARKER_PATTERNS.module.test(message),
    bugfix: MARKER_PATTERNS.bugfix.test(message),
    docs: MARKER_PATTERNS.docs.test(message),
    refactor: MARKER_PATTERNS.refactor.test(message),
  };
}

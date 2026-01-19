# Copilot Instructions for AskPlexNavidrome

## Project Overview
- **AskPlexNavidrome** is an Alexa skill for playing music from a user's Plex Media Server (PMS) or Navidrome server, serving as an alternative to the official Plex skill.
- The Lambda function (entry: `lambda/lambda_function.py`) is the main handler for Alexa requests, orchestrating media playback, intent handling, and state management.
- The project supports both Plex and Subsonic-compatible (Navidrome) backends, with unified logic in `MediaService`.

## Key Components
- **lambda/askplex/**: Core logic for media search, queueing, and playback.
  - `controller.py`: Main Alexa intent and playback controller, coordinates between Alexa SDK and media services.
  - `media_service.py`: Unified interface for searching/playing from Plex and Navidrome.
  - `plex_api.py` / `subsonic_api.py`: API wrappers for Plex and Subsonic-compatible servers.
  - `media_queue.py`: Manages play queue, history, and playback modes.
  - `track.py`: Data model for audio tracks.
  - `config.py`: Loads environment-based configuration for server URLs, tokens, feature flags.
  - `language_strings.json`: Localized prompt templates for Alexa responses.
  - `prompts.py`: Symbolic constants for prompt keys.
- **skill.json**: Alexa skill manifest, defines endpoint and supported locales.
- **interactionModels/custom/**: Alexa interaction models for each locale.

## Developer Workflows
- **Dependencies**: Managed in `lambda/requirements.txt` (uses `boto3`, `ask-sdk`, `plexapi`, `py-sonic`).
- **Configuration**: All runtime config is via environment variables (see `config.py` for names/defaults).
- **Testing/Debugging**: No explicit test suite; debugging is via logs (set `SKILL_LOG_LEVEL` in env or `config.py`).
- **Deployment**: Lambda handler is `lambda_function.lambda_handler`. Ensure all dependencies are packaged for AWS Lambda.

## Project-Specific Patterns
- **Multi-Source Playback**: `MediaService` abstracts over Plex and Navidrome; feature flags (`ENABLE_PLEX`, `ENABLE_NAVIDROME`) control which are active.
- **Queue Management**: `MediaQueue` uses a deque for current, history, and buffer tracks; supports normal, repeat, and loop modes.
- **Prompt Localization**: All Alexa responses use keys from `prompts.py` and templates in `language_strings.json` (multi-language support).
- **Error Handling**: User-facing errors are mapped to localized prompts; internal errors are logged.
- **Skill Logging**: Logging is initialized in `lambda_function.py` and respects the configured log level.

## Integration Points
- **Plex**: Requires server URL and token; uses `plexapi` for media access.
- **Navidrome/Subsonic**: Requires server URL, user, password, port, API location/version; uses `py-sonic`/`libsonic`.
- **DynamoDB**: Used for Alexa persistence (see `lambda_function.py` for adapter setup).

## Examples
- To add a new intent, update `controller.py` and the relevant interaction model in `interactionModels/custom/`.
- To support a new locale, add translations to `language_strings.json` and a new model file.
- To change server config, update environment variables or `config.py` defaults.

---
For more, see the [README.md](../README.md) and [AskPlex Wiki](https://github.com/andresponte/askplex/wiki).

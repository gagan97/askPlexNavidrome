import logging

logger = logging.getLogger(__name__)


def sanitise_speech_output(speech_string: str) -> str:
    """Sanitise speech output inline with the SSML standard

    Speech Synthesis Markup Language (SSML) has certain ASCII characters that are
    reserved.  This function replaces them with alternatives.

    :param speech_string: The string to process
    :type speech_string: str
    :return: The processed SSML compliant string
    :rtype: str
    """

    logger.debug('In sanitise_speech_output()')

    if '&' in speech_string:
        speech_string = speech_string.replace('&', 'and')
    if '/' in speech_string:
        speech_string = speech_string.replace('/', 'and')
    if '\\' in speech_string:
        speech_string = speech_string.replace('\\', 'and')
    if '"' in speech_string:
        speech_string = speech_string.replace('"', '')
    if "'" in speech_string:
        speech_string = speech_string.replace("'", "")
    if "<" in speech_string:
        speech_string = speech_string.replace('<', '')
    if ">" in speech_string:
        speech_string = speech_string.replace('>', '')

    return speech_string


def truncate_for_speech(text: str, max_length: int = 50) -> str:
    """Truncate text for speech output to avoid overly long announcements

    :param text: The text to truncate
    :param max_length: Maximum length before truncation
    :return: Truncated text
    :rtype: str
    """
    if not text or len(text) <= max_length:
        return text

    # Remove common filler patterns that make titles too long
    # Split by common separators and take just the first meaningful part
    separators = [' | ', ' - ', ' / ', ' || ', ' // ', ' : ']
    for sep in separators:
        if sep in text:
            parts = text.split(sep)
            # Take first part if it's substantial enough (more than 3 chars)
            if len(parts[0].strip()) > 3:
                text = parts[0].strip()
                break

    # Remove common suffix patterns
    suffix_patterns = [
        ' FULL SONG', ' Full Song', ' full song',
        ' OFFICIAL VIDEO', ' Official Video', ' official video',
        ' AUDIO', ' Audio', ' audio',
        ' LYRICAL', ' Lyrical', ' lyrical',
        ' HD', ' HQ', ' 4K',
    ]
    for pattern in suffix_patterns:
        if text.endswith(pattern):
            text = text[:-len(pattern)].strip()

    # If still too long, truncate at word boundary
    if len(text) > max_length:
        truncated = text[:max_length]
        # Try to cut at last space to avoid cutting mid-word
        last_space = truncated.rfind(' ')
        if last_space > max_length // 2:
            truncated = truncated[:last_space]
        text = truncated.strip()

    return text


def build_card_data(speech: str, track_details=None, app_name: str = 'AskPlex') -> dict:
    """Build card data dictionary with art URLs from track details.
    
    :param str speech: The speech text to display
    :param track_details: Track object containing cover_art_url and background_url
    :param str app_name: Application name for card title
    :return: Card data dictionary with title, text, art_url, and background_url
    :rtype: dict
    """
    card = {
        'title': app_name,
        'text': speech,
        'art_url': None,
        'background_url': None
    }
    
    if track_details:
        card['art_url'] = getattr(track_details, 'cover_art_url', None)
        card['background_url'] = getattr(track_details, 'background_url', None)
    
    return card

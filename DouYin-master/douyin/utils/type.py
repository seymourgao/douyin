import os

mimes_map = {
    'txt': 'text/plain',
    'htm': 'text/html',
    'html': 'text/html',
    'php': 'text/html',
    'css': 'text/css',
    'js': 'application/javascript',
    'json': 'application/json',
    'xml': 'application/xml',
    'swf': 'application/x-shockwave-flash',
    'flv': 'video/x-flv',
    
    # images
    'png': 'image/png',
    'jpe': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'gif': 'image/gif',
    'bmp': 'image/bmp',
    'ico': 'image/vnd.microsoft.icon',
    'tiff': 'image/tiff',
    'tif': 'image/tiff',
    'svg': 'image/svg+xml',
    'svgz': 'image/svg+xml',
    
    # archives
    'zip': 'application/zip',
    'rar': 'application/x-rar-compressed',
    'exe': 'application/x-msdownload',
    'msi': 'application/x-msdownload',
    'cab': 'application/vnd.ms-cab-compressed',
    
    # audio/video
    'mp3': 'audio/mpeg',
    'ogg': 'audio/ogg',
    'qt': 'video/quicktime',
    'mp4': 'video/mp4',
    'mov': 'video/quicktime',
    'wav': 'audio/x-wav',
    'avi': 'application/octet-stream',
    
    # adobe
    'pdf': 'application/pdf',
    'psd': 'image/vnd.adobe.photoshop',
    'ai': 'application/postscript',
    'eps': 'application/postscript',
    'ps': 'application/postscript',
    
    # ms office
    'doc': 'application/msword',
    'rtf': 'application/rtf',
    'xls': 'application/vnd.ms-excel',
    'ppt': 'application/vnd.ms-powerpoint',
    
    # open office
    'odt': 'application/vnd.oasis.opendocument.text',
    'ods': 'application/vnd.oasis.opendocument.spreadsheet',
}

exts_map = {v: k for k, v in mimes_map.items()}


def ext_to_mime(ext):
    """
    extension to mime
    :param ext: str
    :rtype: str
    """
    if ext in mimes_map.keys():
        return mimes_map[ext]
    else:
        return 'application/octet-stream'


def mime_to_ext(mime):
    """
    mime to extension
    :param mime:
    :return:
    """
    if mime in exts_map.keys():
        return exts_map[mime]
    else:
        return ''

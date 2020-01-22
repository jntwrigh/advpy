import contextlib
import io

sbuf = io.StringIO()
with contextlib.redirect_stdout(sbuf):
    print('This goes into the helptools buffer.')
    print('So does this.')

print('Result:\n{0}'.format(sbuf.getvalue()))

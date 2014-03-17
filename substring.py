# Problem 1.
# Given 2 strings, give me the index of the first occurance of the 2nd string in the 1st string.
# Return -1 if there is no occurance.

# Case-insensitive.
# Whitespace-sensitive.

# Don't use obvious library functions that will make this easy.
# Think of it as though you're writing this in C.

# Problem 2.
# Find any non-contiguous substring within a that matches b.
# If you don't find any string return the largest string that matches
# starting at the front of the second string.
# Ex: aabbcc, abc, returns "abc".
# Ex: aabbcc, abcd, returns "abc".

# Problem 3.
# Ex: cattac cat = cattac
# Ex: cata cat = cat
# Ex: ccaattaacc cat = cattac

def substring3( a, b ):
    if a is None or b is None:
        return None
    bLen = len( b )
    if bLen == 0:
        return ''

    answer = ''
    bPtr = 0
    delta = 1
    for char in a:
        if char == b[ bPtr ]:
            answer += char

            if bPtr < 0:
                break
            elif bPtr == bLen - 1 and delta > 0:
                delta = -delta
                continue
            bPtr += delta

    return answer

def substring2( a, b ):
    if a is None or b is None:
        return None

    answer = ''
    bPtr = 0
    bLen = len( b )
    # The earliest number is the best number.
    # There will never be a case where taking a later number gives you the solution you want
    # because the later number can always be substituted for the earliest number.
    for char in a:
        if bPtr >= bLen:
            break
        if char == b[ bPtr ]:
            answer += char
            bPtr += 1
    return answer

def substring( a, b ):
    def _substring( a, b, index ):
        if a is None or b is None:
            return -1
        if b == '':
            return 0 # An empty string exists as the first occurance always.
        if len( b ) > len( a ):
            return -1
        for i in range( len( b ) ):
            if a[i].lower() != b[i].lower():
                return _substring( a[1:], b, index+1 )
        return index
    return _substring( a, b, 0 )

class TestCase():
    def __init__( self, a, b ):
        self.a = a
        self.b = b
    def run( self ):
        self.answer = substring( self.a, self.b )
    def check( self ):
        # Account for differences between python's 'find' method and our substring method.
        if self.a is None or self.b is None:
            return -1
        else:
            return self.a.lower().find( self.b.lower() ) == self.answer

class TestCase2( TestCase ):
    def run( self ):
        self.answer = substring2( self.a, self.b )
    def check( self ):
        print self.answer
        # Check by visual inspection.

class TestCase3( TestCase2 ):
    def run( self ):
        self.answer = substring3( self.a, self.b )

tests = [ TestCase( None, 'something' ),
          TestCase( 'something', None ),
          TestCase( '', 'something' ),
          TestCase( 'something', '' ),
          TestCase( None, None ),
          TestCase( '', '' ),

          TestCase( 'alexis', 'a' ),
          TestCase( 'alexis', 's' ),
          TestCase( 'alexis', 'x' ),
          TestCase( 'alexis', 'ex' ),
          TestCase( 'alexis', 'alexiss' ),
          TestCase( 'alexis', 'alexis' ),

          TestCase( 'alexis', 'joel' ),
          TestCase( 'alexis', 'alexiz' ),
          TestCase( 'alexis', 'xiz' ),

          TestCase( 'Alexis', 'alexis' ),
          TestCase( 'alexis', 'aLeXiS' ),
          TestCase( ' a l e x i s', 'a l e x i s ' ),
          TestCase( 'alex is', 'x is' ),

          TestCase( "aaaba","aaba" ),
          ]

def testSubstring():
    failed = []
    for test in tests:
        print "test:", test.a, test.b,
        test.run()
        if test.check():
            print "pass:", test.answer
        else:
            print "fail!", test.answer
            failed.append( test )
    print "Total failed:", len( failed )

tests2 = []
for test in tests:
    tests2.append( TestCase2( test.a, test.b ) )
tests2 += [ TestCase2( 'aabbcc', 'abc' ),
            TestCase2( 'aabbcc', 'abcd' ),
            TestCase2( 'alexis', 'eis' ),
            ]

def testSubstring2():
    for test in tests2:
        print "test:", test.a, test.b,
        test.run()
        test.check()

tests3 = []
for test in tests2:
    tests3.append( TestCase3( test.a, test.b ) )
tests3 += [ TestCase3( 'cattac', 'cat' ),
            TestCase3( 'cata', 'cat' ),
            TestCase3( 'ccaattaacc', 'cat' ),
            TestCase3( 'alexxis', 'x' ),
            ]

def testSubstring3():
    for test in tests3:
        print "test:", test.a, test.b,
        test.run()
        test.check()

if __name__ == "__main__":
    #testSubstring()
    #testSubstring2()
    testSubstring3()

######################################################################
##
##  Demonstration - An expression evaluator with history
##
##  This demonstration illustrates development of an
##  interactive program which is made robust to
##  user-input errors through exception handling.
##


#---------------------------------------------------------------------
#
# Requirements specification
#
# The IDLE interpreter's interactive shell window keeps a history
# which allows the last value returned to be referenced via the
# special variable '_'.
#
# The aim here is to develop a generalisation of this concept
# as an expression evaluation environment that keeps
# a history of all returned values and allows the nth value returned
# to be displayed by entering 'Recall n'.  The user can stop the
# program by typing 'Quit'.
# 


#---------------------------------------------------------------------
#
# Fragile version
#
# This version of the expression evaluator works perfectly as
# long as the user never makes an error, but will crash if
# given an unexpected input value.
#
# Try it with the following inputs in the order shown:
#
# 1 + 5
# 'bb' + 'ccc'
# 4 * 'd'
# recall 1
# 34 + 89
# recall 2
# recall 0
# 4 ** 4
# a * n      <- This input will cause a crash
# 'a' + 45   <- So will this one
# recall 8   <- And so will this one
# Control-C  <- And this will stop the program inelegantly
#
def fragile_history():
    
    history = []
    while True:
        user_expression = input('[' + str(len(history)) + '] >>> ')
        if user_expression.lower() == 'quit':
            # User wants to stop
            print('Goodbye')
            break
        elif user_expression.lower().startswith('recall '):
            # User wants to see the value of a previous expression
            print(history[eval(user_expression[7:])])
        else:
            # Evaluate the user's expression
            history = history + [eval(user_expression)]
            print(history[-1])


#---------------------------------------------------------------------
#
# Robust version
#
# This version of the expression evaluator can never crash because
# it catches all exceptions.  For certain anticipated kinds of input
# error it displays a meaningful error message.
#
def robust_history():
    
    history = []
    while True:
        # This is the 'normal' program behaviour, as before
        try: 
            user_expression = input('[' + str(len(history)) + '] >>> ')
            if user_expression.lower() == 'quit':
                # User wants to stop
                print('Goodbye')
                break
            elif user_expression.lower().startswith('recall '):
                # User wants to see the value of a previous expression
                print(history[eval(user_expression[7:])])
            else:
                # Evaluate the user's expression
                history = history + [eval(user_expression)]
                print(history[-1])

        # Catch errors
        except NameError:
            print('Unknown variable')
        except TypeError:
            print('Operator used with arguments of incorrect type')
        except SyntaxError:
            print('Expression is not well-formed')
        except IndexError:
            print('Index value is out of range')
        except KeyboardInterrupt: # Assume user is trying to quit
            print('Goodbye')
            break
        except: # All other exceptions are caught here
            print('Warning: System error - attempting to continue')


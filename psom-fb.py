import bottle
import sys


TESTS = [{'name': 'TEST 1',
         'items': ['item 11', 'item 21', 'item 31'],
         'choices': ['choice 11', 'choice 21', 'choice 31'],
         'scores': [11, 21, 31]},

         {'name': 'TEST 2',
         'items': ['item 12', 'item 22', 'item 32'],
         'choices': ['choice 12', 'choice 22', 'choice 32'],
         'scores': [12, 22, 32]}]


ITEM_TEMPLATE = '''
        <h1>{{testname}}</h1><br>

        <form action="/" method="post">
            {{itemtext}} <br><br>

            <input type="radio" name="itemscore" value="0" /> {{choice1}} <br>
            <input type="radio" name="itemscore" value="1" /> {{choice2}} <br>
            <input type="radio" name="itemscore" value="2" /> {{choice3}} <br><br>

            <input type="submit" value="weiter"><br><br>
        </form>
    '''


item_number = 0
test_number = 0


@bottle.get('/')
def show_item():
    global item_number, test_number

    item_template = bottle.template(ITEM_TEMPLATE, testname=TESTS[test_number]['name'],
                                                   itemtext=TESTS[test_number]['items'][item_number],
                                                   choice1=TESTS[test_number]['choices'][0],
                                                   choice2=TESTS[test_number]['choices'][1],
                                                   choice3=TESTS[test_number]['choices'][2])

    last_item = len(TESTS[test_number]['items']) - 1
    last_test = len(TESTS) - 1

    if item_number > last_item:
        item_number = 0
        if test_number > last_test:
            sys.exit()
        else:
            test_number += 1
    else:
        item_number += 1

    return item_template


@bottle.post('/')
def process_item():
    global item_number, test_number

    item_score = bottle.request.forms.get('itemscore')
    print(item_score)
    print('{test} {item} score: {score}'.format(test=TESTS[test_number]['name'],
                                                item=TESTS[test_number]['items'][item_number],
                                                score=str(item_score)))
    return

if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(host='localhost', port=8080, reloader=True)
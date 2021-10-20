# mit `str.format()`

'my string {} {}'.format(4, 'vier')
# in Reihenfolge der Argumente

'my string {number} {name}'.format(name='vier', number=4)`
# via Name, Reihenfolge egal

'my string {number} {}'.format('vier', number=4)
# oder beides kombiniert

# und mit dem %-Operator

'my string %d %s' % (4, 'vier')
# in Reihenfolge

'my string %(number)d %(name)s' % {'number':4, 'name':'vier'}
# via Name

# mit f strings

f'my string {4} {"vier"}'
# mit f vor dem String, und geschweiften Klammern"

f"my string {4} {'vier'}"
# oder so

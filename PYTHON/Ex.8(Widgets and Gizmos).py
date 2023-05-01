# PROGRAM THAT COMPUTES THE TOTAL WEIGHT OF AN ORDER
print('1 widget weighs 75g while 1 gizmo weighs 112g')
weight_of_widget = 75
weight_of_gizmo = 112
widget_order = int(input('How many widgets do you want? '))
gizmo_order = int(input('How many gizmos do you want? '))
total_order = weight_of_widget * widget_order + weight_of_gizmo * gizmo_order
print(total_order,'g is the total weight of your order.')
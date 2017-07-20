# for more information on where the basis for this function came from, check :
# http://www.dyn4j.org/2010/01/sat/
# It has been adapted to our needs, as well tweaked for use with circles

def checkCollisions(element, element_list, show=True):
    special = ["Circle", "Point"]
    test_type = element.getType()
    base_axes = element.getAxes()
    for component in element_list:
        if component is not element:
            # we consider points the same as circle with a radius of 1
            if test_type in special:
                # if both elements are "circle", we check the distance bewteen their centers
                if component.getType() in special:
                    center_1 = element.getCenter()
                    center_2 = component.getCenter()
                    dis_1_2 = ((center_1[0]-center_2[0])**2 + (center_1[1]-center_2[1])**2)**0.5
                    # if the distance is lower than the sum of their radius, they do not intersect
                    if (dis_1_2 <= component.getRadius()+element.getRadius()):
                        if show:
                            print("Intersection of "+test_type+" with "+component.getType())
                        return True
                # in case of a circle with another type of element, we use the axes we get from the other element
                else:
                    # We got some problems using only the axis of the non-circle element
                    center = element.getCenter()
                    axes = component.getAxes()
                    corners = component.getCorners()
                    # we thus added axes that link the center of the circle to each corner of the element
                    for corner in corners:
                        axes.append([center[0]-corner[0],center[1]-corner[1]])
                    inside = True
                    for axe in axes:
                        element_1 = element.project(axe)
                        element_2 = component.project(axe)
                        if (element_1[0]>element_2[1]) or (element_1[1]<element_2[0]):
                            inside = False
                    if inside:
                        if show:
                            print("Intersection of "+test_type+" with "+component.getType())
                        return True
            # if we don't have a circle or a point, we take the axes, and deduct using the projection on these
            else:
                inside = True
                if component.getType() in special:
                    axes = element.getAxes()
                    center = component.getCenter()
                    corners = element.getCorners()
                    for corner in corners:
                        axes.append([center[0]-corner[0],center[1]-corner[1]])
                else:
                    axes = base_axes + component.getAxes()
                for axe in axes:
                    element_1 = element.project(axe)
                    element_2 = component.project(axe)
                    if (element_1[0]>element_2[1]) or (element_1[1]<element_2[0]):
                        inside = False
                if inside:
                    if show:
                        print("Intersection of "+test_type+" with "+component.getType())
                    return True
    return False

---
title: "DrawOrderType enum - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-drawordertype"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/DrawOrderType-enum-sidebar.html">

<div>

# <span class="kind-enum">DrawOrderType</span> enum

</div>

<div class="section desc markdown">

Specifies the type of map item draw order.

Map item rendering behavior is chosen based on the draw order type.

Regardless of a draw order type map items with a higher draw order are drawn on top of map items with a lower draw order.

When having map items in a scene with the same draw order, but with different draw order types <a href="sdk-for-flutter-explore-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a> and <a href="sdk-for-flutter-explore-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderIndependent</a>, <a href="sdk-for-flutter-explore-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a> items will be rendered on top of <a href="sdk-for-flutter-explore-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderIndependent</a> ones.

</div>

## Values

<span class="name">mapSceneAdditionOrderDependent</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-drawordertype">DrawOrderType</a></span>  
Draw order depends on the order of map item addition to a map scene.

Multiple map items of the same type with the same draw order are drawn in the order of addition to a map scene. With this behavior map items are rendered one by one.

<span class="name">mapSceneAdditionOrderIndependent</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-drawordertype">DrawOrderType</a></span>  
Draw order does not depend on the order of map item addition to a map scene.

Multiple map items of the same type with the same draw order are drawn in an arbitrary order and map items with similar attributes (e.g. color) are grouped and drawn together all at once for performance reasons. This way map items added/re-added to a map scene lastly may appear below already existing map items with the same draw order.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-drawordertype-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-drawordertype-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-drawordertype-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-drawordertype-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-drawordertype-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-drawordertype-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-mapview-drawordertype-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-drawordertype">DrawOrderType</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>


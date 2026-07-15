---
title: "PointDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-pointdatasource-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/PointDataSource-class-sidebar.html">

<div>

# <span class="kind-class">PointDataSource</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Point data source allows the rendering engine access to the user provided geographical locations and their attributes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-pointdatasource">PointDataSource</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-add">add</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-add-param-point" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-pointdata-class">PointData</a></span> <span class="parameter-name">point</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a new point to the data source.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-addpoints">addPoints</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addPoints-param-points" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-datasource-pointdata-class">PointData</a></span>\></span></span> <span class="parameter-name">points</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds new points to the data source.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-destroy">destroy</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Frees all internally used resources.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-foreach">forEach</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-forEach-param-processor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasourcepointdataprocessor">PointDataSourcePointDataProcessor</a></span> <span class="parameter-name">processor</span></span>) <span class="returntype parameter">→ void</span> </span>  
Iterates through all the points from the data source and passes them to the given processor, one by one.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-removeall">removeAll</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all points from the data source.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-removeif">removeIf</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeIf-param-processor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasourcepointdataprocessor">PointDataSourcePointDataProcessor</a></span> <span class="parameter-name">processor</span></span>) <span class="returntype parameter">→ void</span> </span>  
Iterates through all the points from the data source and passes them to the given inspector, one by one.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasource-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


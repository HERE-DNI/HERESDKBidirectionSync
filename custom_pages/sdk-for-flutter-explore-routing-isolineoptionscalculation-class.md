---
title: "IsolineOptionsCalculation class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-isolineoptionscalculation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IsolineOptionsCalculation-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/IsolineOptionsCalculation-class-sidebar.html">

<div>

# <span class="kind-class">IsolineOptionsCalculation</span> class

</div>

<div class="section desc markdown">

Specifies isoline parameters.

Setting at least one limit to <a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-rangevalues">IsolineOptionsCalculation.rangeValues</a> is mandatory or the calculation will fail.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaults">IsolineOptionsCalculation.withDefaults</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withDefaults-param-rangeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolinerangetype">IsolineRangeType</a></span> <span class="parameter-name">rangeType</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-rangeValues" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">rangeValues</span></span>)</span>  
<li>

`rangeType` The range type.

</li>

<li>

`rangeValues` Range values.

</li>

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaultsandcalculationmode">IsolineOptionsCalculation.withDefaultsAndCalculationMode</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withDefaultsAndCalculationMode-param-rangeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolinerangetype">IsolineRangeType</a></span> <span class="parameter-name">rangeType</span>, </span><span id="sdk-for-flutter-explore-withDefaultsAndCalculationMode-param-rangeValues" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">rangeValues</span>, </span><span id="sdk-for-flutter-explore-withDefaultsAndCalculationMode-param-isolineCalculationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolinecalculationmode">IsolineCalculationMode</a></span> <span class="parameter-name">isolineCalculationMode</span></span>)</span>  
<li>

`rangeType` The range type.

</li>

<li>

`rangeValues` Range values.

</li>

<li>

`isolineCalculationMode` The isoline calculation mode.

</li>

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaultsanddirection">IsolineOptionsCalculation.withDefaultsAndDirection</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withDefaultsAndDirection-param-rangeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolinerangetype">IsolineRangeType</a></span> <span class="parameter-name">rangeType</span>, </span><span id="sdk-for-flutter-explore-withDefaultsAndDirection-param-rangeValues" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">rangeValues</span>, </span><span id="sdk-for-flutter-explore-withDefaultsAndDirection-param-isolineDirection" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routeplacedirection">RoutePlaceDirection</a></span> <span class="parameter-name">isolineDirection</span></span>)</span>  
<li>

`rangeType` The range type.

</li>

<li>

`rangeValues` Range values.

</li>

<li>

`isolineDirection` The isoline direction.

</li>

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withnodefaults">IsolineOptionsCalculation.withNoDefaults</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withNoDefaults-param-rangeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolinerangetype">IsolineRangeType</a></span> <span class="parameter-name">rangeType</span>, </span><span id="sdk-for-flutter-explore-withNoDefaults-param-rangeValues" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">rangeValues</span>, </span><span id="sdk-for-flutter-explore-withNoDefaults-param-isolineCalculationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolinecalculationmode">IsolineCalculationMode</a></span> <span class="parameter-name">isolineCalculationMode</span>, </span><span id="sdk-for-flutter-explore-withNoDefaults-param-maxPoints" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">maxPoints</span>, </span><span id="sdk-for-flutter-explore-withNoDefaults-param-isolineDirection" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routeplacedirection">RoutePlaceDirection</a></span> <span class="parameter-name">isolineDirection</span></span>)</span>  
<li>

`rangeType` The range type.

</li>

<li>

`rangeValues` Range values.

</li>

<li>

`isolineCalculationMode` The isoline calculation mode.

</li>

<li>

`maxPoints` The max points number.

</li>

<li>

`isolineDirection` The isoline direction.

</li>

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-isolinecalculationmode">isolineCalculationMode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-isolinecalculationmode">IsolineCalculationMode</a></span>  
Specifies how isoline calculation is optimized. The default waypoint type is <a href="sdk-for-flutter-explore-routing-isolinecalculationmode">IsolineCalculationMode.balanced</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-isolinedirection">isolineDirection</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routeplacedirection">RoutePlaceDirection</a></span>  
Specifies if calculations will be from or to a specific point. The default isoline direction is <a href="sdk-for-flutter-explore-routing-routeplacedirection">RoutePlaceDirection.departure</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-maxpoints">maxPoints</a></span> <span class="signature">↔ int?</span>  
Limits the number of points in the resulting isoline polygon. If the isoline consists of multiple polygons, the sum of points from all polygons is considered. Note that this parameter does not affect the calculation, but the shape of the polygon. Look at <a href="sdk-for-flutter-explore-routing-isolinecalculationmode">IsolineCalculationMode</a> parameter to optimize performance. A higher value will result in a more accurate polygon shape. Rendering a polygon with a high number of points can negatively impact rendering performance. The minimum allowed value is 30, lower values will be ignored.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-rangetype">rangeType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-isolinerangetype">IsolineRangeType</a></span>  
Specifies the range of values to be included in the isoline.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-rangevalues">rangeValues</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
A list of ranges. The unit is defined by the type parameter. Each range defines the maximum allowed value to reach a destination. For each value an <a href="sdk-for-flutter-explore-routing-isoline-class">Isoline</a> is calculated indicating the reachable area. If empty, <a href="sdk-for-flutter-explore-routing-isolineoptions-class">IsolineOptions</a> object is considered invalid.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "WarningsRegistry class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarningsRegistry-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/WarningsRegistry-class-sidebar.html">

<div>

# <span class="kind-class">WarningsRegistry</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A class that store warning metadata for different warning types.

Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.). Provided by `WarnerEngine` so callers can lookup detailed information about specific warnings.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-warningsregistry">WarningsRegistry</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getbordercrossingwarning">getBorderCrossingWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getBorderCrossingWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a>?</span> </span>  
Returns a border crossing warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getcustomwarning">getCustomWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getCustomWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a>?</span> </span>  
Returns additional data associated with the given custom warning.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getdangerzonewarning">getDangerZoneWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getDangerZoneWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-class">DangerZoneWarning</a>?</span> </span>  
Returns a danger zone warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getenvironmentalzonewarning">getEnvironmentalZoneWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getEnvironmentalZoneWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-class">EnvironmentalZoneWarning</a>?</span> </span>  
Returns environmental zone warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getlanedecreasewarning">getLaneDecreaseWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getLaneDecreaseWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-class">LaneDecreaseWarning</a>?</span> </span>  
Returns a lane decrease warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getlowspeedzonewarning">getLowSpeedZoneWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getLowSpeedZoneWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class">LowSpeedZoneWarning</a>?</span> </span>  
Returns a low speed zone warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getrailwaycrossingwarning">getRailwayCrossingWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getRailwayCrossingWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning</a>?</span> </span>  
Returns a railway crossing warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getrealisticviewwarning">getRealisticViewWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getRealisticViewWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a>?</span> </span>  
Returns a realistic-view warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getroadsignwarning">getRoadSignWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getRoadSignWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a>?</span> </span>  
Returns a road-sign warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getsafetycamerawarning">getSafetyCameraWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getSafetyCameraWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-class">SafetyCameraWarning</a>?</span> </span>  
Returns a safety-camera warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-getschoolzonewarning">getSchoolZoneWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getSchoolZoneWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-class">SchoolZoneWarning</a>?</span> </span>  
Returns a school zone warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-gettollstopwarning">getTollStopWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getTollStopWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-tollstop-class">TollStop</a>?</span> </span>  
Returns a toll stop warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-gettrafficmergewarning">getTrafficMergeWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getTrafficMergeWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-class">TrafficMergeWarning</a>?</span> </span>  
Returns a traffic merge warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-gettruckrestrictionwarning">getTruckRestrictionWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getTruckRestrictionWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class">TruckRestrictionWarning</a>?</span> </span>  
Returns a truck restrictions warning corresponding to the given identifier.

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-warner-warningsregistry-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

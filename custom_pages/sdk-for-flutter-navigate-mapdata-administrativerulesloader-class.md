---
title: "AdministrativeRulesLoader class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-administrativerulesloader-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AdministrativeRulesLoader-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/AdministrativeRulesLoader-class-sidebar.html">

<div>

# <span class="kind-class">AdministrativeRulesLoader</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides the abstract class for the access to the administrative rules available for a country or a state in the local OCM map.

Please be aware that the methods within this classload map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-administrativerulesloader">AdministrativeRulesLoader</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-administrativerulesloader-withengine">AdministrativeRulesLoader.withEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-getadministrativerules">getAdministrativeRules</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getAdministrativeRules-param-countryCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-countrycode">CountryCode</a></span> <span class="parameter-name">countryCode</span>, </span><span id="sdk-for-flutter-navigate-getAdministrativeRules-param-stateCode" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">stateCode</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a></span> </span>  
Synchronously load the administrative rules for the specified country and state.

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-getstatecodes">getStateCodes</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getStateCodes-param-countryCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-countrycode">CountryCode</a></span> <span class="parameter-name">countryCode</span></span>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> </span>  
Synchronously loads the list of state codes from a specified country for which administrative rules are availabe.

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-administrativerulesloader-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

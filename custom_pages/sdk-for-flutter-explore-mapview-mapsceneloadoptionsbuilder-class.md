---
title: "MapSceneLoadOptionsBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLoadOptionsBuilder-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapSceneLoadOptionsBuilder-class-sidebar.html">

<div>

# <span class="kind-class">MapSceneLoadOptionsBuilder</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Builder for creating <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a> instances.

This builder ensures that either a MapScheme or a configuration file is set, but not both.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-mapsceneloadoptionsbuilder">MapSceneLoadOptionsBuilder</a></span><span class="signature">()</span>  
Creates a new builder instance.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-build">build</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a></span> </span>  
Builds the <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a> instance.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-withconfigurationfile">withConfigurationFile</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withConfigurationFile-param-configurationFile" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">configurationFile</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-class">MapSceneLoadOptionsBuilder</a></span> </span>  
Sets the configuration file path to load.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-withdisabledfeatures">withDisabledFeatures</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withDisabledFeatures-param-disabledFeatures" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">disabledFeatures</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-class">MapSceneLoadOptionsBuilder</a></span> </span>  
Sets the features to disable in the new configuration.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-withenabledfeatures">withEnabledFeatures</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withEnabledFeatures-param-enabledFeatures" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">String</span>\></span></span> <span class="parameter-name">enabledFeatures</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-class">MapSceneLoadOptionsBuilder</a></span> </span>  
Sets the features to enable in the new configuration.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-withmapscheme">withMapScheme</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withMapScheme-param-mapScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme</a></span> <span class="parameter-name">mapScheme</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-class">MapSceneLoadOptionsBuilder</a></span> </span>  
Sets the map scheme to load.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-withoverridingmapstyle">withOverridingMapStyle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withOverridingMapStyle-param-overridingMapStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-style-class">Style</a></span> <span class="parameter-name">overridingMapStyle</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-class">MapSceneLoadOptionsBuilder</a></span> </span>  
Sets the style to override what is defined in the scene configuration.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-withwatermarkstyle">withWatermarkStyle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withWatermarkStyle-param-watermarkStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-watermarkstyle">WatermarkStyle</a></span> <span class="parameter-name">watermarkStyle</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-class">MapSceneLoadOptionsBuilder</a></span> </span>  
Sets the watermark style.

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptionsbuilder-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

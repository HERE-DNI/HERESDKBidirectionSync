---
title: "IconProvider class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-iconprovider-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/IconProvider-class-sidebar.html">

<div>

# <span class="kind-class">IconProvider</span> class

</div>

<div class="section desc markdown">

This provider creates icons from a given set of parameters for map content and constraints for icon dimensions for a particular map scheme. The icon creation currently does not rely on map data. Therefore, it works without online connection.

Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-iconprovider">IconProvider</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-mapContext" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">mapContext</span></span>)</span>  
Constructor. `mapContext` The map context instance which is obtained using <a href="sdk-for-flutter-navigate-mapview-mapviewbase-mapcontext">HereMapController.mapContext</a>.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-createroadshieldicon">createRoadShieldIcon</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-createRoadShieldIcon-param-properties" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-class">RoadShieldIconProperties</a></span> <span class="parameter-name">properties</span>, </span><span id="sdk-for-flutter-navigate-createRoadShieldIcon-param-mapScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a></span> <span class="parameter-name">mapScheme</span>, </span><span id="sdk-for-flutter-navigate-createRoadShieldIcon-param-assetType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconproviderassettype">IconProviderAssetType</a></span> <span class="parameter-name">assetType</span>, </span><span id="sdk-for-flutter-navigate-createRoadShieldIcon-param-widthConstraintInPixels" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">widthConstraintInPixels</span>, </span><span id="sdk-for-flutter-navigate-createRoadShieldIcon-param-heightConstraintInPixels" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">heightConstraintInPixels</span>, </span><span id="sdk-for-flutter-navigate-createRoadShieldIcon-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconprovidercallback">IconProviderCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Creates an image displaying a road shield according to the given parameters.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-createvehiclerestrictionicon">createVehicleRestrictionIcon</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-pickingResult" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-pickvehiclerestrictionsresult-class">PickVehicleRestrictionsResult</a></span> <span class="parameter-name">pickingResult</span>, </span><span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-mapScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a></span> <span class="parameter-name">mapScheme</span>, </span><span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-assetType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconproviderassettype">IconProviderAssetType</a></span> <span class="parameter-name">assetType</span>, </span><span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-sizeConstraintsInPixels" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span> <span class="parameter-name">sizeConstraintsInPixels</span>, </span><span id="sdk-for-flutter-navigate-createVehicleRestrictionIcon-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconprovidercallback">IconProviderCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Creates an image representing a vehicle restriction as shown on the map, based on map content picking result.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-createvehiclerestrictioniconwithiconproperties">createVehicleRestrictionIconWithIconProperties</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-createVehicleRestrictionIconWithIconProperties-param-properties" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-vehiclerestrictioniconproperties-class">VehicleRestrictionIconProperties</a></span> <span class="parameter-name">properties</span>, </span><span id="sdk-for-flutter-navigate-createVehicleRestrictionIconWithIconProperties-param-mapScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a></span> <span class="parameter-name">mapScheme</span>, </span><span id="sdk-for-flutter-navigate-createVehicleRestrictionIconWithIconProperties-param-assetType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconproviderassettype">IconProviderAssetType</a></span> <span class="parameter-name">assetType</span>, </span><span id="sdk-for-flutter-navigate-createVehicleRestrictionIconWithIconProperties-param-sizeConstraintsInPixels" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a></span> <span class="parameter-name">sizeConstraintsInPixels</span>, </span><span id="sdk-for-flutter-navigate-createVehicleRestrictionIconWithIconProperties-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconprovidercallback">IconProviderCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Creates an image representing a vehicle restriction as shown on the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


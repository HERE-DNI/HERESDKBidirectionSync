---
title: "NativeBase (API Reference)"
slug: "sdk-for-android-explore-nativebase"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- NativeBase.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../index-all.html">Index</a></li>
<li><a href="../../help-doc.html#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li>Method</li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.NativeBase</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="sdk/core/Angle.html" title="class in com.here.sdk.core">Angle</a></code>, <code><a href="sdk/mapview/AssetsManager.html" title="class in com.here.sdk.mapview">AssetsManager</a></code>, <code><a href="sdk/core/Authentication.html" title="class in com.here.sdk.core">Authentication</a></code>, <code><a href="sdk/core/engine/AuthenticationMode.html" title="class in com.here.sdk.core.engine">AuthenticationMode</a></code>, <code><a href="sdk/core/engine/CatalogVersionHint.html" title="class in com.here.sdk.core.engine">CatalogVersionHint</a></code>, <code><a href="sdk/mapview/datasource/DataAttributes.html" title="class in com.here.sdk.mapview.datasource">DataAttributes</a></code>, <code><a href="sdk/mapview/datasource/DataAttributesAccessor.html" title="class in com.here.sdk.mapview.datasource">DataAttributesAccessor</a></code>, <code><a href="sdk/mapview/datasource/DataAttributesBuilder.html" title="class in com.here.sdk.mapview.datasource">DataAttributesBuilder</a></code>, <code><a href="sdk/mapview/datasource/DataAttributeValue.html" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a></code>, <code><a href="sdk/animation/Easing.html" title="class in com.here.sdk.animation">Easing</a></code>, <code><a href="sdk/search/EVChargingLocation.html" title="class in com.here.sdk.search">EVChargingLocation</a></code>, <code><a href="sdk/search/EVSearchEngine.html" title="class in com.here.sdk.search">EVSearchEngine</a></code>, <code><a href="sdk/gestures/FlingHandler.html" title="class in com.here.sdk.gestures">FlingHandler</a></code>, <code><a href="sdk/gestures/Gestures.html" title="class in com.here.sdk.gestures">Gestures</a></code>, <code><a href="sdk/mapview/HereMap.html" title="class in com.here.sdk.mapview">HereMap</a></code>, <code><a href="sdk/search/IndexRange.html" title="class in com.here.sdk.search">IndexRange</a></code>, <code><a href="sdk/routing/IndoorManeuver.html" title="class in com.here.sdk.routing">IndoorManeuver</a></code>, <code><a href="sdk/routing/IndoorSectionDetails.html" title="class in com.here.sdk.routing">IndoorSectionDetails</a></code>, <code><a href="sdk/routing/Isoline.html" title="class in com.here.sdk.routing">Isoline</a></code>, <code><a href="sdk/routing/IsolineRoutingEngine.html" title="class in com.here.sdk.routing">IsolineRoutingEngine</a></code>, <code><a href="sdk/mapview/JsonStyleFactory.html" title="class in com.here.sdk.mapview">JsonStyleFactory</a></code>, <code><a href="sdk/mapview/datasource/LineData.html" title="class in com.here.sdk.mapview.datasource">LineData</a></code>, <code><a href="sdk/mapview/datasource/LineDataAccessor.html" title="class in com.here.sdk.mapview.datasource">LineDataAccessor</a></code>, <code><a href="sdk/mapview/datasource/LineDataBuilder.html" title="class in com.here.sdk.mapview.datasource">LineDataBuilder</a></code>, <code><a href="sdk/mapview/datasource/LineDataSource.html" title="class in com.here.sdk.mapview.datasource">LineDataSource</a></code>, <code><a href="sdk/mapview/datasource/LineDataSourceBuilder.html" title="class in com.here.sdk.mapview.datasource">LineDataSourceBuilder</a></code>, <code><a href="sdk/mapview/datasource/LineTileDataSource.html" title="class in com.here.sdk.mapview.datasource">LineTileDataSource</a></code>, <code><a href="sdk/mapview/LocationIndicator.html" title="class in com.here.sdk.mapview">LocationIndicator</a></code>, <code><a href="sdk/core/engine/LockingProcess.html" title="class in com.here.sdk.core.engine">LockingProcess</a></code>, <code><a href="sdk/core/engine/LogControl.html" title="class in com.here.sdk.core.engine">LogControl</a></code>, <code><a href="sdk/routing/Maneuver.html" title="class in com.here.sdk.routing">Maneuver</a></code>, <code><a href="sdk/mapview/MapArrow.html" title="class in com.here.sdk.mapview">MapArrow</a></code>, <code><a href="sdk/mapview/MapCamera.html" title="class in com.here.sdk.mapview">MapCamera</a></code>, <code><a href="sdk/mapview/MapCameraAnimation.html" title="class in com.here.sdk.mapview">MapCameraAnimation</a></code>, <code><a href="sdk/mapview/MapCameraAnimationFactory.html" title="class in com.here.sdk.mapview">MapCameraAnimationFactory</a></code>, <code><a href="sdk/mapview/MapCameraKeyframeTrack.html" title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></code>, <code><a href="sdk/mapview/MapCameraLimits.html" title="class in com.here.sdk.mapview">MapCameraLimits</a></code>, <code><a href="sdk/mapview/MapCameraUpdate.html" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code>, <code><a href="sdk/mapview/MapCameraUpdateFactory.html" title="class in com.here.sdk.mapview">MapCameraUpdateFactory</a></code>, <code><a href="sdk/mapview/MapContentSettings.html" title="class in com.here.sdk.mapview">MapContentSettings</a></code>, <code><a href="sdk/mapview/MapContext.html" title="class in com.here.sdk.mapview">MapContext</a></code>, <code><a href="sdk/mapview/MapImage.html" title="class in com.here.sdk.mapview">MapImage</a></code>, <code><a href="sdk/mapview/MapImageOverlay.html" title="class in com.here.sdk.mapview">MapImageOverlay</a></code>, <code><a href="sdk/animation/MapItemKeyFrameTrack.html" title="class in com.here.sdk.animation">MapItemKeyFrameTrack</a></code>, <code><a href="sdk/mapview/MapItemRepresentation.html" title="class in com.here.sdk.mapview">MapItemRepresentation</a></code>, <code><a href="sdk/mapview/MapLayer.html" title="class in com.here.sdk.mapview">MapLayer</a></code>, <code><a href="sdk/mapview/MapLayerBuilder.html" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code>, <code><a href="sdk/mapview/MapLayerMapMeasureDependentStorageLevels.html" title="class in com.here.sdk.mapview">MapLayerMapMeasureDependentStorageLevels</a></code>, <code><a href="sdk/mapview/MapLayerPriority.html" title="class in com.here.sdk.mapview">MapLayerPriority</a></code>, <code><a href="sdk/mapview/MapLayerPriorityBuilder.html" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></code>, <code><a href="sdk/mapview/MapMarker.html" title="class in com.here.sdk.mapview">MapMarker</a></code>, <code><a href="sdk/mapview/MapMarker.TextStyle.html" title="class in com.here.sdk.mapview">MapMarker.TextStyle</a></code>, <code><a href="sdk/mapview/MapMarker3D.html" title="class in com.here.sdk.mapview">MapMarker3D</a></code>, <code><a href="sdk/mapview/MapMarker3DModel.html" title="class in com.here.sdk.mapview">MapMarker3DModel</a></code>, <code><a href="sdk/animation/MapMarkerAnimation.html" title="class in com.here.sdk.animation">MapMarkerAnimation</a></code>, <code><a href="sdk/mapview/MapMarkerCluster.html" title="class in com.here.sdk.mapview">MapMarkerCluster</a></code>, <code><a href="sdk/mapview/MapObjectDescriptor.html" title="class in com.here.sdk.mapview">MapObjectDescriptor</a></code>, <code><a href="sdk/mapview/MapPickResult.html" title="class in com.here.sdk.mapview">MapPickResult</a></code>, <code><a href="sdk/mapview/MapPolygon.html" title="class in com.here.sdk.mapview">MapPolygon</a></code>, <code><a href="sdk/mapview/MapPolyline.html" title="class in com.here.sdk.mapview">MapPolyline</a></code>, <code><a href="sdk/animation/MapPolylineAnimation.html" title="class in com.here.sdk.animation">MapPolylineAnimation</a></code>, <code><a href="sdk/mapview/MapScene.html" title="class in com.here.sdk.mapview">MapScene</a></code>, <code><a href="sdk/mapview/MapScene.MapPickFilter.html" title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a></code>, <code><a href="sdk/mapview/MapSceneLights.html" title="class in com.here.sdk.mapview">MapSceneLights</a></code>, <code><a href="sdk/mapview/MapSceneLoadOptions.html" title="class in com.here.sdk.mapview">MapSceneLoadOptions</a></code>, <code><a href="sdk/mapview/MapSceneLoadOptionsBuilder.html" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></code>, <code><a href="sdk/mapview/Mesh.html" title="class in com.here.sdk.mapview">Mesh</a></code>, <code><a href="sdk/mapview/MeshBuilder.html" title="class in com.here.sdk.mapview">MeshBuilder</a></code>, <code><a href="sdk/core/Metadata.html" title="class in com.here.sdk.core">Metadata</a></code>, <code><a href="sdk/mapview/PickMapContentResult.html" title="class in com.here.sdk.mapview">PickMapContentResult</a></code>, <code><a href="sdk/mapview/PickMapContentResult.TrafficIncidentResult.html" title="class in com.here.sdk.mapview">PickMapContentResult.TrafficIncidentResult</a></code>, <code><a href="sdk/mapview/PickMapItemsResult.html" title="class in com.here.sdk.mapview">PickMapItemsResult</a></code>, <code><a href="sdk/search/Place.html" title="class in com.here.sdk.search">Place</a></code>, <code><a href="sdk/search/PlaceCategory.html" title="class in com.here.sdk.search">PlaceCategory</a></code>, <code><a href="sdk/mapview/datasource/PointData.html" title="class in com.here.sdk.mapview.datasource">PointData</a></code>, <code><a href="sdk/mapview/datasource/PointDataAccessor.html" title="class in com.here.sdk.mapview.datasource">PointDataAccessor</a></code>, <code><a href="sdk/mapview/datasource/PointDataBuilder.html" title="class in com.here.sdk.mapview.datasource">PointDataBuilder</a></code>, <code><a href="sdk/mapview/datasource/PointDataSource.html" title="class in com.here.sdk.mapview.datasource">PointDataSource</a></code>, <code><a href="sdk/mapview/datasource/PointDataSourceBuilder.html" title="class in com.here.sdk.mapview.datasource">PointDataSourceBuilder</a></code>, <code><a href="sdk/mapview/datasource/PointTileDataSource.html" title="class in com.here.sdk.mapview.datasource">PointTileDataSource</a></code>, <code><a href="sdk/mapview/datasource/PolygonData.html" title="class in com.here.sdk.mapview.datasource">PolygonData</a></code>, <code><a href="sdk/mapview/datasource/PolygonDataAccessor.html" title="class in com.here.sdk.mapview.datasource">PolygonDataAccessor</a></code>, <code><a href="sdk/mapview/datasource/PolygonDataBuilder.html" title="class in com.here.sdk.mapview.datasource">PolygonDataBuilder</a></code>, <code><a href="sdk/mapview/datasource/PolygonDataSource.html" title="class in com.here.sdk.mapview.datasource">PolygonDataSource</a></code>, <code><a href="sdk/mapview/datasource/PolygonDataSourceBuilder.html" title="class in com.here.sdk.mapview.datasource">PolygonDataSourceBuilder</a></code>, <code><a href="sdk/mapview/datasource/PolygonTileDataSource.html" title="class in com.here.sdk.mapview.datasource">PolygonTileDataSource</a></code>, <code><a href="sdk/core/PolylineSimplifier.html" title="class in com.here.sdk.core">PolylineSimplifier</a></code>, <code><a href="sdk/mapview/datasource/RasterDataSource.html" title="class in com.here.sdk.mapview.datasource">RasterDataSource</a></code>, <code><a href="sdk/routing/RefreshRouteOptions.html" title="class in com.here.sdk.routing">RefreshRouteOptions</a></code>, <code><a href="sdk/routing/Route.html" title="class in com.here.sdk.routing">Route</a></code>, <code><a href="sdk/routing/RoutingEngine.html" title="class in com.here.sdk.routing">RoutingEngine</a></code>, <code><a href="sdk/gestures/ScaleHandler.html" title="class in com.here.sdk.gestures">ScaleHandler</a></code>, <code><a href="sdk/gestures/ScrollHandler.html" title="class in com.here.sdk.gestures">ScrollHandler</a></code>, <code><a href="sdk/core/engine/SDKBuildInformation.html" title="class in com.here.sdk.core.engine">SDKBuildInformation</a></code>, <code><a href="sdk/core/engine/SDKLogger.html" title="class in com.here.sdk.core.engine">SDKLogger</a></code>, <code><a href="sdk/core/engine/SDKNativeEngine.html" title="class in com.here.sdk.core.engine">SDKNativeEngine</a></code>, <code><a href="sdk/search/SearchEngine.html" title="class in com.here.sdk.search">SearchEngine</a></code>, <code><a href="sdk/routing/Section.html" title="class in com.here.sdk.routing">Section</a></code>, <code><a href="sdk/routing/Span.html" title="class in com.here.sdk.routing">Span</a></code>, <code><a href="sdk/mapview/Style.html" title="class in com.here.sdk.mapview">Style</a></code>, <code><a href="sdk/search/Suggestion.html" title="class in com.here.sdk.search">Suggestion</a></code>, <code><a href="sdk/core/threading/Threading.html" title="class in com.here.sdk.core.threading">Threading</a></code>, <code><a href="sdk/mapview/datasource/TileGeoBoundsCalculator.html" title="class in com.here.sdk.mapview.datasource">TileGeoBoundsCalculator</a></code>, <code><a href="sdk/mapview/datasource/TileUrlProviderFactory.html" title="class in com.here.sdk.mapview.datasource">TileUrlProviderFactory</a></code>, <code><a href="sdk/core/TimeRule.html" title="class in com.here.sdk.core">TimeRule</a></code>, <code><a href="sdk/traffic/TrafficDataProvider.html" title="class in com.here.sdk.traffic">TrafficDataProvider</a></code>, <code><a href="sdk/traffic/TrafficEngine.html" title="class in com.here.sdk.traffic">TrafficEngine</a></code>, <code><a href="sdk/traffic/TrafficFlow.html" title="class in com.here.sdk.traffic">TrafficFlow</a></code>, <code><a href="sdk/traffic/TrafficIncident.html" title="class in com.here.sdk.traffic">TrafficIncident</a></code>, <code><a href="sdk/routing/TrafficIncidentOnRoute.html" title="class in com.here.sdk.routing">TrafficIncidentOnRoute</a></code>, <code><a href="sdk/routing/TransitRoutingEngine.html" title="class in com.here.sdk.routing">TransitRoutingEngine</a></code>, <code><a href="sdk/mapview/TranslucentMapLayerGroup.html" title="class in com.here.sdk.mapview">TranslucentMapLayerGroup</a></code>, <code><a href="sdk/transport/TransportSpecification.BicycleBuilder.html" title="class in com.here.sdk.transport">TransportSpecification.BicycleBuilder</a></code>, <code><a href="sdk/transport/TransportSpecification.BusBuilder.html" title="class in com.here.sdk.transport">TransportSpecification.BusBuilder</a></code>, <code><a href="sdk/transport/TransportSpecification.CarBuilder.html" title="class in com.here.sdk.transport">TransportSpecification.CarBuilder</a></code>, <code><a href="sdk/transport/TransportSpecification.PedestrianBuilder.html" title="class in com.here.sdk.transport">TransportSpecification.PedestrianBuilder</a></code>, <code><a href="sdk/transport/TransportSpecification.PrivateBusBuilder.html" title="class in com.here.sdk.transport">TransportSpecification.PrivateBusBuilder</a></code>, <code><a href="sdk/transport/TransportSpecification.ScooterBuilder.html" title="class in com.here.sdk.transport">TransportSpecification.ScooterBuilder</a></code>, <code><a href="sdk/transport/TransportSpecification.TaxiBuilder.html" title="class in com.here.sdk.transport">TransportSpecification.TaxiBuilder</a></code>, <code><a href="sdk/transport/TransportSpecification.TruckBuilder.html" title="class in com.here.sdk.transport">TransportSpecification.TruckBuilder</a></code>, <code><a href="sdk/transport/VehicleSpecification.BusBuilder.html" title="class in com.here.sdk.transport">VehicleSpecification.BusBuilder</a></code>, <code><a href="sdk/transport/VehicleSpecification.CarBuilder.html" title="class in com.here.sdk.transport">VehicleSpecification.CarBuilder</a></code>, <code><a href="sdk/transport/VehicleSpecification.PrivateBusBuilder.html" title="class in com.here.sdk.transport">VehicleSpecification.PrivateBusBuilder</a></code>, <code><a href="sdk/transport/VehicleSpecification.ScooterBuilder.html" title="class in com.here.sdk.transport">VehicleSpecification.ScooterBuilder</a></code>, <code><a href="sdk/transport/VehicleSpecification.TaxiBuilder.html" title="class in com.here.sdk.transport">VehicleSpecification.TaxiBuilder</a></code>, <code><a href="sdk/transport/VehicleSpecification.TruckBuilder.html" title="class in com.here.sdk.transport">VehicleSpecification.TruckBuilder</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public abstract class </span><span class="element-name type-name-label">NativeBase</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Internal base class for public non-POD objects to manage the lifecycle of underlying C++ objects.
 While the class is public for technical reasons, but should be considered <b>internal</b> and not
 part of the public API and thus not used directly.

 <p>Java classes which wrap C++ objects inherit from NativeBase to
 <ol>
<li>reference the C++ object</li>
<li>manage the lifecycle of C++ object</li>
</ol>
<p>Cleanup of C++ objects is done automatically as long as there are new subclasses of NativeBase
 created. Currently there is no explicit way to destroy the underlying C++ object of a Java
 wrapper. This is intentional because normally no manual cleanup is necessary. Additionally the
 client of the Java wrapper would need additional knowledge of the underlying implementation to
 be able to decide whether or not cleanup is necessary. It is not clear for the client which
 object needs cleanup and which doesn't if all objects have auto-generated cleanup functions.
 So instead API designers should manually define methods if resource cleanup is necessary.</p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>

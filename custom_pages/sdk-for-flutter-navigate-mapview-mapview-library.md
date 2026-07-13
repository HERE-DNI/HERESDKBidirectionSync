---
title: "mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapview-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- mapview-library.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="" data-below-sidebar="mapview/mapview-library-sidebar.html">

<div>

# <span class="kind-library">mapview</span> library

</div>

## Classes

<span class="name"><a href="sdk-for-flutter-navigate-mapview-assetsmanager-class">AssetsManager</a></span>  
Assets manager interface.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-dashpattern-class">DashPattern</a></span>  
Represents a dash pattern for map polyline.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremap-class">HereMap</a></span>  
Widget that displays a map. To interact with the map, use the <a href="sdk-for-flutter-navigate-mapview-heremapcontroller-class">HereMapController</a> object that is passed to <a href="sdk-for-flutter-navigate-mapview-heremapcreatedcallback">HereMapCreatedCallback</a> Note: Before using this class, <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> must be already initialized.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-class">HereMapController</a></span>  
Allows interacting with the map displayed by <a href="sdk-for-flutter-navigate-mapview-heremap-class">HereMap</a> widget.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span>  
The representation of a dynamic and interactive geographic map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapoptions-class">HereMapOptions</a></span>  
Options used for initialization of map view

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovider-class">IconProvider</a></span>  
This provider creates icons from a given set of parameters for map content and constraints for icon dimensions for a particular map scheme. The icon creation currently does not rely on map data. Therefore, it works without online connection.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-jsonstylefactory-class">JsonStyleFactory</a></span>  
A factory of <a href="sdk-for-flutter-navigate-mapview-style-class">Style</a> objects from styles defined in JSON format.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-jsonstylefactoryinstantiationerrordetails-class">JsonStyleFactoryInstantiationErrorDetails</a></span>  
Describes the reason for failing to create a <a href="sdk-for-flutter-navigate-mapview-style-class">Style</a> from a JSON source.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a></span>  
Graphical object to represent the location of the user on the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maparrow-class">MapArrow</a></span>  
A visual representation of an arrow on the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcamera-class">MapCamera</a></span>  
Represents the camera looking onto the map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a></span>  
An animation that can be applied to a <a href="sdk-for-flutter-navigate-mapview-mapcamera-class">MapCamera</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationfactory-class">MapCameraAnimationFactory</a></span>  
Factory for creating MapCameraAnimation objects to change map's camera over time.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcamerafarplaneconfiguration-class">MapCameraFarPlaneConfiguration</a></span>  
Far plane distance configuration for a zoom level.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span>  
Stores keyframes for interpolation of a camera property using a specific easing function and interpolation mode.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameralimits-class">MapCameraLimits</a></span>  
Controls constraints on map camera parameters.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameralistener-class">MapCameraListener</a></span>  
Abstract class for objects that want to get updates whenever the map is redrawn after camera parameters change.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcamerastate-class">MapCameraState</a></span>  
Encapsulates state of the camera.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span>  
An update that can be applied to the map camera.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class">MapCameraUpdateFactory</a></span>  
Factory for creating MapCameraUpdate to change map's camera.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-class">MapContentSettings</a></span>  
Provides settings regarding map data which are applied globally to all map views.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span>  
MapContext is the rendering engine and the context in which virtual geographic maps get rendered.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a></span>  
Memory management options.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-class">MapContextMemoryManagementResult</a></span>  
Memory management result.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-class">MapFeatureModes</a></span>  
Holds constants for map feature modes, to be used with <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeatures-class">MapFeatures</a></span>  
Holds constants for map features, to be used with <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> and <a href="sdk-for-flutter-navigate-mapview-mapscene-disablefeatures">MapScene.disableFeatures</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-class">MapIdleListener</a></span>  
Used to detect when the map becomes idle or busy.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span>  
Represents a drawable resource that can be used by a <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>, <a href="sdk-for-flutter-navigate-mapview-mapmarker3d-class">MapMarker3D</a> or <a href="sdk-for-flutter-navigate-mapview-mapimageoverlay-class">MapImageOverlay</a> to be shown on the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimageoverlay-class">MapImageOverlay</a></span>  
`MapImageOverlay` is used to draw images over the map, at a view coordinate inside the map viewport.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapitemrepresentation-class">MapItemRepresentation</a></span>  
Base class to represent visual style of particular map items.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-class">MapLayer</a></span>  
Interface for managing a map layer.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-class">MapLayerBuilder</a></span>  
MapLayerBuilder is used to add layers to a map to visualise a dataset in a programmatic way without defining it upfront in the configuration files.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerbuilderinstantiationerrordetails-class">MapLayerBuilderInstantiationErrorDetails</a></span>  
Describes the reason for failing to build a <a href="sdk-for-flutter-navigate-mapview-maplayer-class">MapLayer</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a></span>  
Provides a mapping between a MapLayer map measure to datasource storage level.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a></span>  
MapLayerPriority class.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span>  
MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayervisibilityrange-class">MapLayerVisibilityRange</a></span>  
A layer's visibility along a zoom level range.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a></span>  
`MapMarker` is used to draw images on the map, for example to mark a specific location.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker3d-class">MapMarker3D</a></span>  
Represents a 3D shape drawn on the map at specified geodetic coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span>  
Represents a 3D model that can be used by a <a href="sdk-for-flutter-navigate-mapview-mapmarker3d-class">MapMarker3D</a> to be shown on the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-class">MapMarkerCluster</a></span>  
Groups map markers and enables their clustering to reduce visual clutter when there are many of them in a small area.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarkerclustercounterstyle-class">MapMarkerClusterCounterStyle</a></span>  
Styling options for a marker cluster which is represented by the marker count as a text.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarkerclustergrouping-class">MapMarkerClusterGrouping</a></span>  
Represents a group of map markers belonging to a cluster.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarkerclusterimagestyle-class">MapMarkerClusterImageStyle</a></span>  
This class specifies the visual appearance of a cluster marker.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyle-class">MapMarkerTextStyle</a></span>  
Styling options for the text of a <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>  
A map measure.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
Represents a render size, described as map measure dependent values.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a></span>  
A map measure range.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapobjectdescriptor-class">MapObjectDescriptor</a></span>  
Interface represents descriptor of a pickable map object.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappickresult-class">MapPickResult</a></span>  
A class representing a map pick result.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-class">MapPolygon</a></span>  
A visual representation of a polygon on the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-class">MapPolyline</a></span>  
A visual representation of a line on the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-class">MapPolylineDashImageRepresentation</a></span>  
Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-class">MapPolylineDashRepresentation</a></span>  
Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a></span>  
Base class to represent the visual appearance of a <a href="sdk-for-flutter-navigate-mapview-mappolyline-class">MapPolyline</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidmulticolorrepresentation-class">MapPolylineSolidMultiColorRepresentation</a></span>  
Representation allows map polyline to be colored in multiple specified color segments.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-class">MapPolylineSolidRepresentation</a></span>  
Representation for a solid line without outline.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a></span>  
Represents a map scene and exposes the functionality to manipulate its content.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-class">MapSceneLights</a></span>  
Manage the lights and their attributes in a scene.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-class">MapSceneLightsDirection</a></span>  
The direction of lights as a pair of azimuth and altitude angles.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a></span>  
Represents the configuration options for loading a map scene.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptionsbuilder-class">MapSceneLoadOptionsBuilder</a></span>  
Builder for creating <a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a> instances.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptionsbuilderinstantiationerrordetails-class">MapSceneLoadOptionsBuilderInstantiationErrorDetails</a></span>  
Describes the reason for failing to build a <a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenemappickfilter-class">MapSceneMapPickFilter</a></span>  
Filter for the map content to be picked.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span>  
Represents the available public API from `MapView`.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a></span>  
Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-materialreflectivity-class">MaterialReflectivity</a></span>  
Material reflectivity properties are used to enable per‑pixel lighting for supported map objects (e.g.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mesh-class">Mesh</a></span>  
Represents a mesh in 3D space.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a></span>  
Builder for meshes.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-pickmapcontentresult-class">PickMapContentResult</a></span>  
A class that contains possible results from picking map content on the map scene.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-pickmapitemsresult-class">PickMapItemsResult</a></span>  
Carries results from the picking of map items on the map scene.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-picktrafficincidentresult-class">PickTrafficIncidentResult</a></span>  
Carries the result of picking a Carto traffic incident object.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-pickvehiclerestrictionsresult-class">PickVehicleRestrictionsResult</a></span>  
Carries the result of picking a vehicle restriction object.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-quadmeshbuilder-class">QuadMeshBuilder</a></span>  
Builder for a single quad.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-rendersize-class">RenderSize</a></span>  
Represents size of visual elements drawn on the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-class">RoadShieldIconProperties</a></span>  
Contains the information required to create a road shield image.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-style-class">Style</a></span>  
A style that defines the visual appearance of map rendered features.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-translucentmaplayergroup-class">TranslucentMapLayerGroup</a></span>  
A translucent layer group that can be the target for <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-ingroup">MapLayerPriorityBuilder.inGroup</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-translucentmaplayergrouperrordetails-class">TranslucentMapLayerGroupErrorDetails</a></span>  
Describes the reason for failing to create the group.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a></span>  
Builder for a single triangle.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-vehiclerestrictioniconproperties-class">VehicleRestrictionIconProperties</a></span>  
Encapsulates properties for generating vehicle restriction icons using `IconProvider`.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a></span>  
Controller for a `Widget` pinned at a fixed geographical location on the map.

## Enums

<span class="name"><a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType</a></span>  
Specifies the type of map item draw order.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapevent">HereMapEvent</a></span>  

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconproviderassettype">IconProviderAssetType</a></span>  
Asset types for loading icons.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovidererror">IconProviderError</a></span>  
Error which indicates why an icon could not be retrieved.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-imageformat">ImageFormat</a></span>  
Image format.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-jsonstylefactoryinstantiationerrorcode">JsonStyleFactoryInstantiationErrorCode</a></span>  
Describes reasons for failing to create a <a href="sdk-for-flutter-navigate-mapview-style-class">Style</a> from a JSON source.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-linecap">LineCap</a></span>  
Determines the cap (line ending) style.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicatorindicatorstyle">LocationIndicatorIndicatorStyle</a></span>  
The predefined styles for the location indicator which are pedestrian and navigation mode.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicatormarkertype">LocationIndicatorMarkerType</a></span>  
Enum to identify different types of markers of the location indicator.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationerrorcode">MapCameraAnimationInstantiationErrorCode</a></span>  
Describes a reason for failing to create a multi-track <a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrackinstantiationerrorcode">MapCameraKeyframeTrackInstantiationErrorCode</a></span>  
Describes a reason for failing to create a MapCameraKeyframeTrack.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdateinstantiationerrorcode">MapCameraUpdateInstantiationErrorCode</a></span>  
Describes a reason for failing to create a <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentcategory">MapContentCategory</a></span>  
Type representing map content categories.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettingstrafficrefreshperioderrorcode">MapContentSettingsTrafficRefreshPeriodErrorCode</a></span>  
Traffic refresh period error code

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontenttype">MapContentType</a></span>  
Content types supported by the map.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextfreeresourceseverity">MapContextFreeResourceSeverity</a></span>  
The severity of a free resource request.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode">MapContextMemoryManagementResultCode</a></span>  
The memory management result code.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementstrategy">MapContextMemoryManagementStrategy</a></span>  
The memory management strategy.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextresourcetype">MapContextResourceType</a></span>  
Types of system resources used by <a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a> or any of the entities attached to it, like <a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maperror">MapError</a></span>  
Represents various errors that could occur from map related operations.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerbuilderinstantiationerrorcode">MapLayerBuilderInstantiationErrorCode</a></span>  
Describes a reason for failing to build a <a href="sdk-for-flutter-navigate-mapview-maplayer-class">MapLayer</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodelinstantiationerrorcode">MapMarker3DModelInstantiationErrorCode</a></span>  
Indicates the reason for a failure to create <a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyleinstantiationerrorcode">MapMarkerTextStyleInstantiationErrorCode</a></span>  
Describes a reason for failing to create a <a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyle-class">MapMarkerTextStyle</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyleplacement">MapMarkerTextStylePlacement</a></span>  
Represents text placement with respect to the icon of a <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersizeinstantiationerrorcode">MapMeasureDependentRenderSizeInstantiationErrorCode</a></span>  
Describes a reason for failing to create a <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a></span>  
Kinds of measures.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationerrorcode">MapPolylineRepresentationInstantiationErrorCode</a></span>  
Describes a reason for failing to create a <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapprojection">MapProjection</a></span>  
The map projection used for rendering.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maprendermode">MapRenderMode</a></span>  
For Android only: Mode of rendering the map by a `HereMap` widget.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingerror">MapSceneLightsAttributeSettingError</a></span>  
Error enum indicating reasons for failure when setting light attributes.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span>  
The scene uses three categories of lighting which are: Main light, Back light and Rim light.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptionsbuilderinstantiationerrorcode">MapSceneLoadOptionsBuilderInstantiationErrorCode</a></span>  
Describes a reason for failing to build a <a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenemappickfiltercontenttype">MapSceneMapPickFilterContentType</a></span>  
Type of the map content to be picked.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a></span>  
Represents the preconfigured map schemes bundled with the SDK.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-nativeviewmode">NativeViewMode</a></span>  
Mode of hosting native Android view in Flutter

<span class="name"><a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a></span>  
Defines different units in which the size is described.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality</a></span>  
The shadow quality.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-translucentmaplayergrouperrorcode">TranslucentMapLayerGroupErrorCode</a></span>  
Error codes for creating the group.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-visibilitystate">VisibilityState</a></span>  
Represents the visibility state of an SDK map view's object.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-watermarkstyle">WatermarkStyle</a></span>  
Defines the style of the HERE watermark logo.

## Typedefs

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapcreatedcallback">HereMapCreatedCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-HereMapCreatedCallback-param-mapController" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-heremapcontroller-class">HereMapController</a></span> <span class="parameter-name">mapController</span></span>)</span></span> </span>  
Method called when the map is ready to be used.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-heremapeventcallback">HereMapEventCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-event" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-heremapevent">HereMapEvent</a></span> <span class="parameter-name">event</span></span>)</span></span> </span>  

<span class="name"><a href="sdk-for-flutter-navigate-mapview-iconprovidercallback">IconProviderCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-imageInfo" class="parameter"><span class="type-annotation">ImageInfo?</span> <span class="parameter-name">imageInfo</span>, </span><span id="sdk-for-flutter-navigate-param-iconDescription" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">iconDescription</span>, </span><span id="sdk-for-flutter-navigate-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconprovidererror">IconProviderError</a>?</span> <span class="parameter-name">error</span></span>)</span></span> </span>  
A callback of this type is invoked when an icon is received from the <a href="sdk-for-flutter-navigate-mapview-iconprovider-class">IconProvider</a> in the `ImageInfo` format. The callback provides information about the loaded icon, or an <a href="sdk-for-flutter-navigate-mapview-iconprovidererror">IconProviderError</a> if one occurred.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameradrycameraupdatecallback">MapCameraDryCameraUpdateCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-cameraState" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcamerastate-class">MapCameraState</a>?</span> <span class="parameter-name">cameraState</span></span>)</span></span> </span>  
Used to report back results of dry update application to camera.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontextsetmemorymanagementoptionscallback">MapContextSetMemoryManagementOptionsCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-result" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-class">MapContextMemoryManagementResult</a></span> <span class="parameter-name">result</span></span>)</span></span> </span>  
Callback to handle the memory management result.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-setLightError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingerror">MapSceneLightsAttributeSettingError</a>?</span> <span class="parameter-name">setLightError</span></span>)</span></span> </span>  
This callback function allows handling errors that occur during the setting of light attributes.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-loadSceneError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-maperror">MapError</a>?</span> <span class="parameter-name">loadSceneError</span></span>)</span></span> </span>  
Called on the main thread after

    loadScene()

method finishes loading the scene.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewbasemappickcallback">MapViewBaseMapPickCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-mapPickResult" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mappickresult-class">MapPickResult</a>?</span> <span class="parameter-name">mapPickResult</span></span>)</span></span> </span>  
Callback for a pick request.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-takescreenshotcallback">TakeScreenshotCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-image" class="parameter"><span class="type-annotation">ImageInfo?</span> <span class="parameter-name">image</span></span>)</span></span> </span>  
Callback to be called on retrieval of screenshot.

## Exceptions / Errors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-jsonstylefactoryinstantiationexception-class">JsonStyleFactoryInstantiationException</a></span>  
Thrown when failing to create a <a href="sdk-for-flutter-navigate-mapview-style-class">Style</a> from a JSON source.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimationinstantiationexception-class">MapCameraAnimationInstantiationException</a></span>  
Thrown when a problem occurs while trying to create a multi-track <a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a></span>  
Thrown when a problem occurs while trying to create <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdateinstantiationexception-class">MapCameraUpdateInstantiationException</a></span>  
Thrown when a problem occurs while trying to create a <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettingstrafficrefreshperiodexceptionexception-class">MapContentSettingsTrafficRefreshPeriodExceptionException</a></span>  
Traffic refresh period error exception

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerbuilderinstantiationexception-class">MapLayerBuilderInstantiationException</a></span>  
Thrown when failing to build a <a href="sdk-for-flutter-navigate-mapview-maplayer-class">MapLayer</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodelinstantiationexception-class">MapMarker3DModelInstantiationException</a></span>  
Thrown when a problem occurs while trying to create <a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyleinstantiationexception-class">MapMarkerTextStyleInstantiationException</a></span>  
Thrown when a problem occurs while trying to create a <a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyle-class">MapMarkerTextStyle</a> instance.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersizeinstantiationexception-class">MapMeasureDependentRenderSizeInstantiationException</a></span>  
Thrown when a problem occurs while trying to create <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a></span>  
Thrown when a problem occurs while trying to create <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptionsbuilderinstantiationexception-class">MapSceneLoadOptionsBuilderInstantiationException</a></span>  
Thrown when failing to build a <a href="sdk-for-flutter-navigate-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-translucentmaplayergroupinstantiationexception-class">TranslucentMapLayerGroupInstantiationException</a></span>  
Thrown when failing to build the group.

</div>

<!-- /.main-content --> <!--/sidebar-offcanvas-right--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

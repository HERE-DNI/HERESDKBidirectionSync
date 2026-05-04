---
title: "com.here.sdk.mapview (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpackage-summary"
hidden: false
---

# Package com.here.sdk.mapview

------------------------------------------------------------------------
package com.here.sdk.mapview

Related Packages

Package

  Description

  [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes
  Exceptions

  Class

  Description

  [AssetsManager](sdk-for-android-explore-api-reference-latestassetsmanager "class in com.here.sdk.mapview")

Assets manager interface.

[DashPattern](sdk-for-android-explore-api-reference-latestdashpattern "class in com.here.sdk.mapview")

Represents a dash pattern for map polyline.

[DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")

Specifies the type of map item draw order.

[HereMap](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview")

The representation of a dynamic and interactive geographic map.

[IconProvider](sdk-for-android-explore-api-reference-latesticonprovider "class in com.here.sdk.mapview")

This provider creates icons from a given set of parameters for map content and constraints for icon dimensions for a particular map scheme.

[IconProvider.IconCallback](sdk-for-android-explore-api-reference-latesticonprovider-iconcallback "interface in com.here.sdk.mapview")

Interface which is used as callback to pass back an image or error code after calling the createRoadShieldIcon() method.

[IconProviderAssetType](sdk-for-android-explore-api-reference-latesticonproviderassettype "enum class in com.here.sdk.mapview")

Asset types for loading icons.

[IconProviderError](sdk-for-android-explore-api-reference-latesticonprovidererror "enum class in com.here.sdk.mapview")

Error which indicates why an icon could not be retrieved.

[ImageFormat](sdk-for-android-explore-api-reference-latestimageformat "enum class in com.here.sdk.mapview")

Image format.

[JsonStyleFactory](sdk-for-android-explore-api-reference-latestjsonstylefactory "class in com.here.sdk.mapview")

A factory of [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") objects from styles defined in JSON format.

[JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes reasons for failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.

[JsonStyleFactory.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrordetails "class in com.here.sdk.mapview")

Describes the reason for failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.

[JsonStyleFactory.InstantiationException](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationexception "class in com.here.sdk.mapview")

Thrown when failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.

[LineCap](sdk-for-android-explore-api-reference-latestlinecap "enum class in com.here.sdk.mapview")

Determines the cap (line ending) style.

[LocationIndicator](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview")

Graphical object to represent the location of the user on the map.

[LocationIndicator.IndicatorStyle](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview")

The predefined styles for the location indicator which are pedestrian and navigation mode.

[LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")

Enum to identify different types of markers of the location indicator.

[MapArrow](sdk-for-android-explore-api-reference-latestmaparrow "class in com.here.sdk.mapview")

A visual representation of an arrow on the map.

[MapCamera](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview")

Represents the camera looking onto the map view.

[MapCamera.DryCameraUpdateCallback](sdk-for-android-explore-api-reference-latestmapcamera-drycameraupdatecallback "interface in com.here.sdk.mapview")

Used to report back results of dry update application to camera.

[MapCamera.FarPlaneConfiguration](sdk-for-android-explore-api-reference-latestmapcamera-farplaneconfiguration "class in com.here.sdk.mapview")

Far plane distance configuration for a zoom level.

[MapCamera.State](sdk-for-android-explore-api-reference-latestmapcamera-state "class in com.here.sdk.mapview")

Encapsulates state of the camera.

[MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")

An animation that can be applied to a [`MapCamera`](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview").

[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes a reason for failing to create a multi-track [`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview").

[MapCameraAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationexception "class in com.here.sdk.mapview")

Thrown when a problem occurs while trying to create a multi-track [`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview").

[MapCameraAnimationFactory](sdk-for-android-explore-api-reference-latestmapcameraanimationfactory "class in com.here.sdk.mapview")

Factory for creating MapCameraAnimation objects to change map's camera over time.

[MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")

Stores keyframes for interpolation of a camera property using a specific easing function and interpolation mode.

[MapCameraKeyframeTrack.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes a reason for failing to create a MapCameraKeyframeTrack.

[MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")

Thrown when a problem occurs while trying to create [`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview").

[MapCameraLimits](sdk-for-android-explore-api-reference-latestmapcameralimits "class in com.here.sdk.mapview")

Controls constraints on map camera parameters.

[MapCameraListener](sdk-for-android-explore-api-reference-latestmapcameralistener "interface in com.here.sdk.mapview")

Interface for objects that want to get updates whenever the map is redrawn after camera parameters change.

[MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

An update that can be applied to the map camera.

[MapCameraUpdate.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraupdate-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes a reason for failing to create a [`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview").

[MapCameraUpdate.InstantiationException](sdk-for-android-explore-api-reference-latestmapcameraupdate-instantiationexception "class in com.here.sdk.mapview")

Thrown when a problem occurs while trying to create a [`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview").

[MapCameraUpdateFactory](sdk-for-android-explore-api-reference-latestmapcameraupdatefactory "class in com.here.sdk.mapview")

Factory for creating MapCameraUpdate to change map's camera.

[MapContentCategory](sdk-for-android-explore-api-reference-latestmapcontentcategory "enum class in com.here.sdk.mapview")

Type representing map content categories.

[MapContentSettings](sdk-for-android-explore-api-reference-latestmapcontentsettings "class in com.here.sdk.mapview")

Provides settings regarding map data which are applied globally to all map views.

[MapContentSettings.TrafficRefreshPeriodErrorCode](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperioderrorcode "enum class in com.here.sdk.mapview")

Traffic refresh period error code

[MapContentSettings.TrafficRefreshPeriodException](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperiodexception "class in com.here.sdk.mapview")

Traffic refresh period error exception

[MapContentType](sdk-for-android-explore-api-reference-latestmapcontenttype "enum class in com.here.sdk.mapview")

Content types supported by the map.

[MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")

MapContext is the rendering engine and the context in which virtual geographic maps get rendered.

[MapContext.FreeResourceSeverity](sdk-for-android-explore-api-reference-latestmapcontext-freeresourceseverity "enum class in com.here.sdk.mapview")

The severity of a free resource request.

[MapContext.MemoryManagementOptions](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions "class in com.here.sdk.mapview")

Memory management options.

[MapContext.MemoryManagementResult](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresult "class in com.here.sdk.mapview")

Memory management result.

[MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")

The memory management result code.

[MapContext.MemoryManagementStrategy](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementstrategy "enum class in com.here.sdk.mapview")

The memory management strategy.

[MapContext.ResourceType](sdk-for-android-explore-api-reference-latestmapcontext-resourcetype "enum class in com.here.sdk.mapview")

Types of system resources used by [`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") or any of the entities attached to it, like [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview").

[MapContext.SetMemoryManagementOptionsCallback](sdk-for-android-explore-api-reference-latestmapcontext-setmemorymanagementoptionscallback "interface in com.here.sdk.mapview")

Callback to handle the memory management result.

[MapError](sdk-for-android-explore-api-reference-latestmaperror "enum class in com.here.sdk.mapview")

Represents various errors that could occur from map related operations.

[MapFeatureModes](sdk-for-android-explore-api-reference-latestmapfeaturemodes "class in com.here.sdk.mapview")

Holds constants for map feature modes, to be used with [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)).

[MapFeatures](sdk-for-android-explore-api-reference-latestmapfeatures "class in com.here.sdk.mapview")

Holds constants for map features, to be used with [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) and [`MapScene.disableFeatures(java.util.List<java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#disableFeatures(java.util.List)).

[MapIdleListener](sdk-for-android-explore-api-reference-latestmapidlelistener "interface in com.here.sdk.mapview")

Used to detect when the map becomes idle or busy.

[MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")

Represents a drawable resource that can be used by a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview"), [`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") or [`MapImageOverlay`](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview") to be shown on the map.

[MapImageFactory](sdk-for-android-explore-api-reference-latestmapimagefactory "class in com.here.sdk.mapview")

Convenience factory class for loading marker resources from various sources.

[MapImageOverlay](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview")

`MapImageOverlay` is used to draw images over the map, at a view coordinate inside the map viewport.

[MapItemRepresentation](sdk-for-android-explore-api-reference-latestmapitemrepresentation "class in com.here.sdk.mapview")

Base class to represent visual style of particular map items.

[MapLayer](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview")

Interface for managing a map layer.

[MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

MapLayerBuilder is used to add layers to a map to visualise a dataset in a programmatic way without defining it upfront in the configuration files.

[MapLayerBuilder.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes a reason for failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").

[MapLayerBuilder.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrordetails "class in com.here.sdk.mapview")

Describes the reason for failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").

[MapLayerBuilder.InstantiationException](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationexception "class in com.here.sdk.mapview")

Thrown when failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").

[MapLayerMapMeasureDependentStorageLevels](sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview")

Provides a mapping between a MapLayer map measure to datasource storage level.

[MapLayerPriority](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview")

MapLayerPriority class.

[MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs.

[MapLayerVisibilityRange](sdk-for-android-explore-api-reference-latestmaplayervisibilityrange "class in com.here.sdk.mapview")

A layer's visibility along a zoom level range.

[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")

`MapMarker` is used to draw images on the map, for example to mark a specific location.

[MapMarker.TextStyle](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview")

Styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

[MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes a reason for failing to create a [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview").

[MapMarker.TextStyle.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview")

Thrown when a problem occurs while trying to create a [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview") instance.

[MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")

Represents text placement with respect to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

[MapMarker3D](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")

Represents a 3D shape drawn on the map at specified geodetic coordinates.

[MapMarker3DModel](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview")

Represents a 3D model that can be used by a [`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") to be shown on the map.

[MapMarker3DModel.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview")

Indicates the reason for a failure to create [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").

[MapMarker3DModel.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview")

Thrown when a problem occurs while trying to create [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").

[MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")

Groups map markers and enables their clustering to reduce visual clutter when there are many of them in a small area.

[MapMarkerCluster.CounterStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-counterstyle "class in com.here.sdk.mapview")

Styling options for a marker cluster which is represented by the marker count as a text.

[MapMarkerCluster.Grouping](sdk-for-android-explore-api-reference-latestmapmarkercluster-grouping "class in com.here.sdk.mapview")

Represents a group of map markers belonging to a cluster.

[MapMarkerCluster.ImageStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-imagestyle "class in com.here.sdk.mapview")

This class specifies the visual appearance of a cluster marker.

[MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")

A map measure.

[MapMeasure.Kind](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview")

Kinds of measures.

[MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

Represents a render size, described as map measure dependent values.

[MapMeasureDependentRenderSize.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes a reason for failing to create a [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview").

[MapMeasureDependentRenderSize.InstantiationException](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview")

Thrown when a problem occurs while trying to create [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview").

[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")

A map measure range.

[MapObjectDescriptor](sdk-for-android-explore-api-reference-latestmapobjectdescriptor "class in com.here.sdk.mapview")

Interface represents descriptor of a pickable map object.

[MapPickResult](sdk-for-android-explore-api-reference-latestmappickresult "class in com.here.sdk.mapview")

A class representing a map pick result.

[MapPolygon](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")

A visual representation of a polygon on the map.

[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")

A visual representation of a line on the map.

[MapPolyline.DashImageRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-dashimagerepresentation "class in com.here.sdk.mapview")

Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.

[MapPolyline.DashRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-dashrepresentation "class in com.here.sdk.mapview")

Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.

[MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")

Base class to represent the visual appearance of a [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview").

[MapPolyline.Representation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes a reason for failing to create a [`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview").

[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

Thrown when a problem occurs while trying to create [`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview").

[MapPolyline.SolidRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-solidrepresentation "class in com.here.sdk.mapview")

Representation for a solid line without outline.

[MapProjection](sdk-for-android-explore-api-reference-latestmapprojection "enum class in com.here.sdk.mapview")

The map projection used for rendering.

[MapRenderMode](sdk-for-android-explore-api-reference-latestmaprendermode "enum class in com.here.sdk.mapview")

Mode of rendering the map by a `MapView`.

[MapScene](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview")

Represents a map scene and exposes the functionality to manipulate its content.

[MapScene.LoadSceneCallback](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview")

Called on the main thread after `loadScene()` method finishes loading the scene.

[MapScene.MapPickFilter](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview")

Filter for the map content to be picked.

[MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")

Type of the map content to be picked.

[MapSceneLights](sdk-for-android-explore-api-reference-latestmapscenelights "class in com.here.sdk.mapview")

Manage the lights and their attributes in a scene.

[MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback "interface in com.here.sdk.mapview")

This callback function allows handling errors that occur during the setting of light attributes.

[MapSceneLights.AttributeSettingError](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingerror "enum class in com.here.sdk.mapview")

Error enum indicating reasons for failure when setting light attributes.

[MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")

The scene uses three categories of lighting which are: Main light, Back light and Rim light.

[MapSceneLights.Direction](sdk-for-android-explore-api-reference-latestmapscenelights-direction "class in com.here.sdk.mapview")

The direction of lights as a pair of azimuth and altitude angles.

[MapSceneLoadOptions](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview")

Represents the configuration options for loading a map scene.

[MapSceneLoadOptionsBuilder](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

Builder for creating [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview") instances.

[MapSceneLoadOptionsBuilder.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationerrorcode "enum class in com.here.sdk.mapview")

Describes a reason for failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").

[MapSceneLoadOptionsBuilder.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationerrordetails "class in com.here.sdk.mapview")

Describes the reason for failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").

[MapSceneLoadOptionsBuilder.InstantiationException](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationexception "class in com.here.sdk.mapview")

Thrown when failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").

[MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")

Represents the preconfigured map schemes bundled with the SDK.

[MapSurface](sdk-for-android-explore-api-reference-latestmapsurface "class in com.here.sdk.mapview")

Provides the ability to render a map into a provided rendering surface.

[MapSurface.RenderListener](sdk-for-android-explore-api-reference-latestmapsurface-renderlistener "interface in com.here.sdk.mapview")

Listener of MapSurface render events.

[MapView](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview")

A view that can display a map.

[MapView.OnReadyListener](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview")

Listener that gets notified when MapView is fully initialized and ready to handle all operations, which means that map scene is loaded and drawing surface is ready to render a map.

[MapView.TakeScreenshotCallback](sdk-for-android-explore-api-reference-latestmapview-takescreenshotcallback "interface in com.here.sdk.mapview")

Callback to be called on retrieval of screenshot.

[MapView.ViewPin](sdk-for-android-explore-api-reference-latestmapview-viewpin "interface in com.here.sdk.mapview")

A ViewPin is used to display Android views at a fixed location on the map.

[MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

Represents the available public API from `MapView`.

[MapViewBase.MapPickCallback](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview")

Callback for a pick request.

[MapViewLifecycleListener](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")

Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.

[MapViewOptions](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview")

Options used for initialization of map view

[MaterialReflectivity](sdk-for-android-explore-api-reference-latestmaterialreflectivity "class in com.here.sdk.mapview")

Material reflectivity properties are used to enable per‑pixel lighting for supported map objects (e.g.

[Mesh](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview")

Represents a mesh in 3D space.

[MeshBuilder](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview")

Builder for meshes.

[PickMapContentResult](sdk-for-android-explore-api-reference-latestpickmapcontentresult "class in com.here.sdk.mapview")

A class that contains possible results from picking map content on the map scene.

[PickMapContentResult.TrafficIncidentResult](sdk-for-android-explore-api-reference-latestpickmapcontentresult-trafficincidentresult "class in com.here.sdk.mapview")

Carries the result of picking a Carto traffic incident object.

[PickMapItemsResult](sdk-for-android-explore-api-reference-latestpickmapitemsresult "class in com.here.sdk.mapview")

Carries results from the picking of map items on the map scene.

[QuadMeshBuilder](sdk-for-android-explore-api-reference-latestquadmeshbuilder "class in com.here.sdk.mapview")

Builder for a single quad.

[RenderSize](sdk-for-android-explore-api-reference-latestrendersize "class in com.here.sdk.mapview")

Represents size of visual elements drawn on the map.

[RenderSize.Unit](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview")

Defines different units in which the size is described.

[RoadShieldIconProperties](sdk-for-android-explore-api-reference-latestroadshieldiconproperties "class in com.here.sdk.mapview")

Contains the information required to create a road shield image.

[ShadowQuality](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview")

The shadow quality.

[Style](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview")

A style that defines the visual appearance of map rendered features.

[TranslucentMapLayerGroup](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup "class in com.here.sdk.mapview")

A translucent layer group that can be the target for [`MapLayerPriorityBuilder.inGroup(java.lang.String)`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder#inGroup(java.lang.String)).

[TranslucentMapLayerGroup.ErrorCode](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errorcode "enum class in com.here.sdk.mapview")

Error codes for creating the group.

[TranslucentMapLayerGroup.ErrorDetails](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errordetails "class in com.here.sdk.mapview")

Describes the reason for failing to create the group.

[TranslucentMapLayerGroup.InstantiationException](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview")

Thrown when failing to build the group.

[TriangleMeshBuilder](sdk-for-android-explore-api-reference-latesttrianglemeshbuilder "class in com.here.sdk.mapview")

Builder for a single triangle.

[VisibilityState](sdk-for-android-explore-api-reference-latestvisibilitystate "enum class in com.here.sdk.mapview")

Represents the visibility state of an SDK map view's object.

[WatermarkStyle](sdk-for-android-explore-api-reference-latestwatermarkstyle "enum class in com.here.sdk.mapview")

Defines the style of the HERE watermark logo.

---
title: "com.here.sdk.mapview (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-package-summary"
---

<div class="package-signature">

package <span class="element-name">com.here.sdk.mapview</span>

</div>

<div class="section summary">

- <div id="related-package-summary">

  <div class="caption">

  Related Packages

  </div>

  | Package | Description |
  |----|----|
  | [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary) |   |

  </div>

- <div id="class-summary">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes
  Exceptions

  </div>

  <div id="class-summary.tabpanel" aria-labelledby="class-summary-tab0"
  role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-assetsmanager"
  title="class in com.here.sdk.mapview">AssetsManager</a></td>
  <td><div class="block">
  Assets manager interface.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-dashpattern"
  title="class in com.here.sdk.mapview">DashPattern</a></td>
  <td><div class="block">
  Represents a dash pattern for map polyline.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-drawordertype"
  title="enum class in com.here.sdk.mapview">DrawOrderType</a></td>
  <td><div class="block">
  Specifies the type of map item draw order.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-heremap"
  title="class in com.here.sdk.mapview">HereMap</a></td>
  <td><div class="block">
  The representation of a dynamic and interactive geographic map.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-iconprovider"
  title="class in com.here.sdk.mapview">IconProvider</a></td>
  <td><div class="block">
  This provider creates icons from a given set of parameters for map
  content and constraints for icon dimensions for a particular map scheme.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-iconprovider-iconcallback"
  title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a></td>
  <td><div class="block">
  Interface which is used as callback to pass back an image or error code
  after calling the createRoadShieldIcon() method.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-iconproviderassettype"
  title="enum class in com.here.sdk.mapview">IconProviderAssetType</a></td>
  <td><div class="block">
  Asset types for loading icons.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-iconprovidererror"
  title="enum class in com.here.sdk.mapview">IconProviderError</a></td>
  <td><div class="block">
  Error which indicates why an icon could not be retrieved.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-imageformat"
  title="enum class in com.here.sdk.mapview">ImageFormat</a></td>
  <td><div class="block">
  Image format.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory"
  title="class in com.here.sdk.mapview">JsonStyleFactory</a></td>
  <td><div class="block">
  A factory of Style objects from styles defined in JSON format.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">JsonStyleFactory.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes reasons for failing to create a Style from a JSON source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory-instantiationerrordetails"
  title="class in com.here.sdk.mapview">JsonStyleFactory.InstantiationErrorDetails</a></td>
  <td><div class="block">
  Describes the reason for failing to create a Style from a JSON source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory-instantiationexception"
  title="class in com.here.sdk.mapview">JsonStyleFactory.InstantiationException</a></td>
  <td><div class="block">
  Thrown when failing to create a Style from a JSON source.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-linecap"
  title="enum class in com.here.sdk.mapview">LineCap</a></td>
  <td><div class="block">
  Determines the cap (line ending) style.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-locationindicator"
  title="class in com.here.sdk.mapview">LocationIndicator</a></td>
  <td><div class="block">
  Graphical object to represent the location of the user on the map.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-locationindicator-indicatorstyle"
  title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a></td>
  <td><div class="block">
  The predefined styles for the location indicator which are pedestrian
  and navigation mode.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-locationindicator-markertype"
  title="enum class in com.here.sdk.mapview">LocationIndicator.MarkerType</a></td>
  <td><div class="block">
  Enum to identify different types of markers of the location indicator.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-maparrow"
  title="class in com.here.sdk.mapview">MapArrow</a></td>
  <td><div class="block">
  A visual representation of an arrow on the map.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera"
  title="class in com.here.sdk.mapview">MapCamera</a></td>
  <td><div class="block">
  Represents the camera looking onto the map view.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-drycameraupdatecallback"
  title="interface in com.here.sdk.mapview">MapCamera.DryCameraUpdateCallback</a></td>
  <td><div class="block">
  Used to report back results of dry update application to camera.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-farplaneconfiguration"
  title="class in com.here.sdk.mapview">MapCamera.FarPlaneConfiguration</a></td>
  <td><div class="block">
  Far plane distance configuration for a zoom level.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state"
  title="class in com.here.sdk.mapview">MapCamera.State</a></td>
  <td><div class="block">
  Encapsulates state of the camera.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation"
  title="class in com.here.sdk.mapview">MapCameraAnimation</a></td>
  <td><div class="block">
  An animation that can be applied to a MapCamera .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapCameraAnimation.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes a reason for failing to create a multi-track
  MapCameraAnimation .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationexception"
  title="class in com.here.sdk.mapview">MapCameraAnimation.InstantiationException</a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create a multi-track
  MapCameraAnimation .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimationfactory"
  title="class in com.here.sdk.mapview">MapCameraAnimationFactory</a></td>
  <td><div class="block">
  Factory for creating MapCameraAnimation objects to change map's camera
  over time.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamerakeyframetrack"
  title="class in com.here.sdk.mapview">MapCameraKeyframeTrack</a></td>
  <td><div class="block">
  Stores keyframes for interpolation of a camera property using a specific
  easing function and interpolation mode.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes a reason for failing to create a MapCameraKeyframeTrack.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamerakeyframetrack-instantiationexception"
  title="class in com.here.sdk.mapview">MapCameraKeyframeTrack.InstantiationException</a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create
  MapCameraKeyframeTrack .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameralimits"
  title="class in com.here.sdk.mapview">MapCameraLimits</a></td>
  <td><div class="block">
  Controls constraints on map camera parameters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameralistener"
  title="interface in com.here.sdk.mapview">MapCameraListener</a></td>
  <td><div class="block">
  Interface for objects that want to get updates whenever the map is
  redrawn after camera parameters change.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview">MapCameraUpdate</a></td>
  <td><div class="block">
  An update that can be applied to the map camera.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapCameraUpdate.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes a reason for failing to create a MapCameraUpdate .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate-instantiationexception"
  title="class in com.here.sdk.mapview">MapCameraUpdate.InstantiationException</a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create a MapCameraUpdate .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdatefactory"
  title="class in com.here.sdk.mapview">MapCameraUpdateFactory</a></td>
  <td><div class="block">
  Factory for creating MapCameraUpdate to change map's camera.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentcategory"
  title="enum class in com.here.sdk.mapview">MapContentCategory</a></td>
  <td><div class="block">
  Type representing map content categories.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings"
  title="class in com.here.sdk.mapview">MapContentSettings</a></td>
  <td><div class="block">
  Provides settings regarding map data which are applied globally to all
  map views.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperioderrorcode"
  title="enum class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodErrorCode</a></td>
  <td><div class="block">
  Traffic refresh period error code
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception"
  title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></td>
  <td><div class="block">
  Traffic refresh period error exception
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontenttype"
  title="enum class in com.here.sdk.mapview">MapContentType</a></td>
  <td><div class="block">
  Content types supported by the map.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext"
  title="class in com.here.sdk.mapview">MapContext</a></td>
  <td><div class="block">
  MapContext is the rendering engine and the context in which virtual
  geographic maps get rendered.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-freeresourceseverity"
  title="enum class in com.here.sdk.mapview">MapContext.FreeResourceSeverity</a></td>
  <td><div class="block">
  The severity of a free resource request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions"
  title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a></td>
  <td><div class="block">
  Memory management options.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresult"
  title="class in com.here.sdk.mapview">MapContext.MemoryManagementResult</a></td>
  <td><div class="block">
  Memory management result.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode"
  title="enum class in com.here.sdk.mapview">MapContext.MemoryManagementResultCode</a></td>
  <td><div class="block">
  The memory management result code.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementstrategy"
  title="enum class in com.here.sdk.mapview">MapContext.MemoryManagementStrategy</a></td>
  <td><div class="block">
  The memory management strategy.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-resourcetype"
  title="enum class in com.here.sdk.mapview">MapContext.ResourceType</a></td>
  <td><div class="block">
  Types of system resources used by MapContext or any of the entities
  attached to it, like HereMap .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback"
  title="interface in com.here.sdk.mapview">MapContext.SetMemoryManagementOptionsCallback</a></td>
  <td><div class="block">
  Callback to handle the memory management result.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-maperror"
  title="enum class in com.here.sdk.mapview">MapError</a></td>
  <td><div class="block">
  Represents various errors that could occur from map related operations.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes"
  title="class in com.here.sdk.mapview">MapFeatureModes</a></td>
  <td><div class="block">
  Holds constants for map feature modes, to be used with
  MapScene.enableFeatures(java.util.Map ) .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapfeatures"
  title="class in com.here.sdk.mapview">MapFeatures</a></td>
  <td><div class="block">
  Holds constants for map features, to be used with
  MapScene.enableFeatures(java.util.Map ) and
  MapScene.disableFeatures(java.util.List ) .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapidlelistener"
  title="interface in com.here.sdk.mapview">MapIdleListener</a></td>
  <td><div class="block">
  Used to detect when the map becomes idle or busy.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapimage"
  title="class in com.here.sdk.mapview">MapImage</a></td>
  <td><div class="block">
  Represents a drawable resource that can be used by a MapMarker ,
  MapMarker3D or MapImageOverlay to be shown on the map.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapimagefactory"
  title="class in com.here.sdk.mapview">MapImageFactory</a></td>
  <td><div class="block">
  Convenience factory class for loading marker resources from various
  sources.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapimageoverlay"
  title="class in com.here.sdk.mapview">MapImageOverlay</a></td>
  <td><div class="block">
  MapImageOverlay is used to draw images over the map, at a view
  coordinate inside the map viewport.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapitemrepresentation"
  title="class in com.here.sdk.mapview">MapItemRepresentation</a></td>
  <td><div class="block">
  Base class to represent visual style of particular map items.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayer"
  title="class in com.here.sdk.mapview">MapLayer</a></td>
  <td><div class="block">
  Interface for managing a map layer.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview">MapLayerBuilder</a></td>
  <td><div class="block">
  MapLayerBuilder is used to add layers to a map to visualise a dataset in
  a programmatic way without defining it upfront in the configuration
  files.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapLayerBuilder.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes a reason for failing to build a MapLayer .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder-instantiationerrordetails"
  title="class in com.here.sdk.mapview">MapLayerBuilder.InstantiationErrorDetails</a></td>
  <td><div class="block">
  Describes the reason for failing to build a MapLayer .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder-instantiationexception"
  title="class in com.here.sdk.mapview">MapLayerBuilder.InstantiationException</a></td>
  <td><div class="block">
  Thrown when failing to build a MapLayer .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayermapmeasuredependentstoragelevels"
  title="class in com.here.sdk.mapview">MapLayerMapMeasureDependentStorageLevels</a></td>
  <td><div class="block">
  Provides a mapping between a MapLayer map measure to datasource storage
  level.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority"
  title="class in com.here.sdk.mapview">MapLayerPriority</a></td>
  <td><div class="block">
  MapLayerPriority class.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder"
  title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></td>
  <td><div class="block">
  MapLayerPriorityBuilder is an interface used to define the rendering
  priority of a layer and its categories, relative to other layers or
  layer-category pairs.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayervisibilityrange"
  title="class in com.here.sdk.mapview">MapLayerVisibilityRange</a></td>
  <td><div class="block">
  A layer's visibility along a zoom level range.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker"
  title="class in com.here.sdk.mapview">MapMarker</a></td>
  <td><div class="block">
  MapMarker is used to draw images on the map, for example to mark a
  specific location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle"
  title="class in com.here.sdk.mapview">MapMarker.TextStyle</a></td>
  <td><div class="block">
  Styling options for the text of a MapMarker .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes a reason for failing to create a MapMarker.TextStyle .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception"
  title="class in com.here.sdk.mapview">MapMarker.TextStyle.InstantiationException</a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create a
  MapMarker.TextStyle instance.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-placement"
  title="enum class in com.here.sdk.mapview">MapMarker.TextStyle.Placement</a></td>
  <td><div class="block">
  Represents text placement with respect to the icon of a MapMarker .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d"
  title="class in com.here.sdk.mapview">MapMarker3D</a></td>
  <td><div class="block">
  Represents a 3D shape drawn on the map at specified geodetic
  coordinates.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel"
  title="class in com.here.sdk.mapview">MapMarker3DModel</a></td>
  <td><div class="block">
  Represents a 3D model that can be used by a MapMarker3D to be shown on
  the map.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapMarker3DModel.InstantiationErrorCode</a></td>
  <td><div class="block">
  Indicates the reason for a failure to create MapMarker3DModel .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception"
  title="class in com.here.sdk.mapview">MapMarker3DModel.InstantiationException</a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create MapMarker3DModel .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster"
  title="class in com.here.sdk.mapview">MapMarkerCluster</a></td>
  <td><div class="block">
  Groups map markers and enables their clustering to reduce visual clutter
  when there are many of them in a small area.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle"
  title="class in com.here.sdk.mapview">MapMarkerCluster.CounterStyle</a></td>
  <td><div class="block">
  Styling options for a marker cluster which is represented by the marker
  count as a text.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping"
  title="class in com.here.sdk.mapview">MapMarkerCluster.Grouping</a></td>
  <td><div class="block">
  Represents a group of map markers belonging to a cluster.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-imagestyle"
  title="class in com.here.sdk.mapview">MapMarkerCluster.ImageStyle</a></td>
  <td><div class="block">
  This class specifies the visual appearance of a cluster marker.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasure"
  title="class in com.here.sdk.mapview">MapMeasure</a></td>
  <td><div class="block">
  A map measure.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasure-kind"
  title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a></td>
  <td><div class="block">
  Kinds of measures.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize"
  title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></td>
  <td><div class="block">
  Represents a render size, described as map measure dependent values.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapMeasureDependentRenderSize.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes a reason for failing to create a MapMeasureDependentRenderSize
  .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception"
  title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize.InstantiationException</a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create
  MapMeasureDependentRenderSize .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange"
  title="class in com.here.sdk.mapview">MapMeasureRange</a></td>
  <td><div class="block">
  A map measure range.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapobjectdescriptor"
  title="class in com.here.sdk.mapview">MapObjectDescriptor</a></td>
  <td><div class="block">
  Interface represents descriptor of a pickable map object.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mappickresult"
  title="class in com.here.sdk.mapview">MapPickResult</a></td>
  <td><div class="block">
  A class representing a map pick result.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mappolygon"
  title="class in com.here.sdk.mapview">MapPolygon</a></td>
  <td><div class="block">
  A visual representation of a polygon on the map.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline"
  title="class in com.here.sdk.mapview">MapPolyline</a></td>
  <td><div class="block">
  A visual representation of a line on the map.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-dashimagerepresentation"
  title="class in com.here.sdk.mapview">MapPolyline.DashImageRepresentation</a></td>
  <td><div class="block">
  Represents a dash pattern for the map polyline consisting of images
  rendered with certain gaps from each other.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-dashrepresentation"
  title="class in com.here.sdk.mapview">MapPolyline.DashRepresentation</a></td>
  <td><div class="block">
  Represents a dash pattern for map polyline where the dash can be
  rendered as a colored line and the gap can be either empty or colored.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation"
  title="class in com.here.sdk.mapview">MapPolyline.Representation</a></td>
  <td><div class="block">
  Base class to represent the visual appearance of a MapPolyline .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes a reason for failing to create a MapPolyline.Representation .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception"
  title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create
  MapPolyline.Representation .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation"
  title="class in com.here.sdk.mapview">MapPolyline.SolidMultiColorRepresentation</a></td>
  <td><div class="block">
  Representation allows map polyline to be colored in multiple specified
  color segments.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidrepresentation"
  title="class in com.here.sdk.mapview">MapPolyline.SolidRepresentation</a></td>
  <td><div class="block">
  Representation for a solid line without outline.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapprojection"
  title="enum class in com.here.sdk.mapview">MapProjection</a></td>
  <td><div class="block">
  The map projection used for rendering.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-maprendermode"
  title="enum class in com.here.sdk.mapview">MapRenderMode</a></td>
  <td><div class="block">
  Mode of rendering the map by a MapView .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapscene"
  title="class in com.here.sdk.mapview">MapScene</a></td>
  <td><div class="block">
  Represents a map scene and exposes the functionality to manipulate its
  content.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscene-loadscenecallback"
  title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a></td>
  <td><div class="block">
  Called on the main thread after loadScene() method finishes loading the
  scene.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscene-mappickfilter"
  title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a></td>
  <td><div class="block">
  Filter for the map content to be picked.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscene-mappickfilter-contenttype"
  title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a></td>
  <td><div class="block">
  Type of the map content to be picked.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights"
  title="class in com.here.sdk.mapview">MapSceneLights</a></td>
  <td><div class="block">
  Manage the lights and their attributes in a scene.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback"
  title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a></td>
  <td><div class="block">
  This callback function allows handling errors that occur during the
  setting of light attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingerror"
  title="enum class in com.here.sdk.mapview">MapSceneLights.AttributeSettingError</a></td>
  <td><div class="block">
  Error enum indicating reasons for failure when setting light attributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-category"
  title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a></td>
  <td><div class="block">
  The scene uses three categories of lighting which are: Main light, Back
  light and Rim light.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-direction"
  title="class in com.here.sdk.mapview">MapSceneLights.Direction</a></td>
  <td><div class="block">
  The direction of lights as a pair of azimuth and altitude angles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptions"
  title="class in com.here.sdk.mapview">MapSceneLoadOptions</a></td>
  <td><div class="block">
  Represents the configuration options for loading a map scene.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder"
  title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></td>
  <td><div class="block">
  Builder for creating MapSceneLoadOptions instances.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationErrorCode</a></td>
  <td><div class="block">
  Describes a reason for failing to build a MapSceneLoadOptions .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationerrordetails"
  title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationErrorDetails</a></td>
  <td><div class="block">
  Describes the reason for failing to build a MapSceneLoadOptions .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationexception"
  title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationException</a></td>
  <td><div class="block">
  Thrown when failing to build a MapSceneLoadOptions .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapscheme"
  title="enum class in com.here.sdk.mapview">MapScheme</a></td>
  <td><div class="block">
  Represents the preconfigured map schemes bundled with the SDK.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapsurface"
  title="class in com.here.sdk.mapview">MapSurface</a></td>
  <td><div class="block">
  Provides the ability to render a map into a provided rendering surface.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsurface-renderlistener"
  title="interface in com.here.sdk.mapview">MapSurface.RenderListener</a></td>
  <td><div class="block">
  Listener of MapSurface render events.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapview"
  title="class in com.here.sdk.mapview">MapView</a></td>
  <td><div class="block">
  A view that can display a map.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapview-onreadylistener"
  title="interface in com.here.sdk.mapview">MapView.OnReadyListener</a></td>
  <td><div class="block">
  Listener that gets notified when MapView is fully initialized and ready
  to handle all operations, which means that map scene is loaded and
  drawing surface is ready to render a map.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapview-takescreenshotcallback"
  title="interface in com.here.sdk.mapview">MapView.TakeScreenshotCallback</a></td>
  <td><div class="block">
  Callback to be called on retrieval of screenshot.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapview-viewpin"
  title="interface in com.here.sdk.mapview">MapView.ViewPin</a></td>
  <td><div class="block">
  A ViewPin is used to display Android views at a fixed location on the
  map.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapviewbase"
  title="interface in com.here.sdk.mapview">MapViewBase</a></td>
  <td><div class="block">
  Represents the available public API from MapView .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapviewbase-mappickcallback"
  title="interface in com.here.sdk.mapview">MapViewBase.MapPickCallback</a></td>
  <td><div class="block">
  Callback for a pick request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapviewlifecyclelistener"
  title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a></td>
  <td><div class="block">
  Provides a mechanism for observing a lifecycle of a map view and/or
  implementing components whose lifecycle needs to be linked with that of
  a map view.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapviewoptions"
  title="class in com.here.sdk.mapview">MapViewOptions</a></td>
  <td><div class="block">
  Options used for initialization of map view
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-materialreflectivity"
  title="class in com.here.sdk.mapview">MaterialReflectivity</a></td>
  <td><div class="block">
  Material reflectivity properties are used to enable per‑pixel lighting
  for supported map objects (e.g.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mesh"
  title="class in com.here.sdk.mapview">Mesh</a></td>
  <td><div class="block">
  Represents a mesh in 3D space.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder"
  title="class in com.here.sdk.mapview">MeshBuilder</a></td>
  <td><div class="block">
  Builder for meshes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult"
  title="class in com.here.sdk.mapview">PickMapContentResult</a></td>
  <td><div class="block">
  A class that contains possible results from picking map content on the
  map scene.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult-trafficincidentresult"
  title="class in com.here.sdk.mapview">PickMapContentResult.TrafficIncidentResult</a></td>
  <td><div class="block">
  Carries the result of picking a Carto traffic incident object.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-pickmapitemsresult"
  title="class in com.here.sdk.mapview">PickMapItemsResult</a></td>
  <td><div class="block">
  Carries results from the picking of map items on the map scene.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-quadmeshbuilder"
  title="class in com.here.sdk.mapview">QuadMeshBuilder</a></td>
  <td><div class="block">
  Builder for a single quad.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-rendersize"
  title="class in com.here.sdk.mapview">RenderSize</a></td>
  <td><div class="block">
  Represents size of visual elements drawn on the map.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit"
  title="enum class in com.here.sdk.mapview">RenderSize.Unit</a></td>
  <td><div class="block">
  Defines different units in which the size is described.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties"
  title="class in com.here.sdk.mapview">RoadShieldIconProperties</a></td>
  <td><div class="block">
  Contains the information required to create a road shield image.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-shadowquality"
  title="enum class in com.here.sdk.mapview">ShadowQuality</a></td>
  <td><div class="block">
  The shadow quality.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-style"
  title="class in com.here.sdk.mapview">Style</a></td>
  <td><div class="block">
  A style that defines the visual appearance of map rendered features.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup"
  title="class in com.here.sdk.mapview">TranslucentMapLayerGroup</a></td>
  <td><div class="block">
  A translucent layer group that can be the target for
  MapLayerPriorityBuilder.inGroup(java.lang.String) .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-errorcode"
  title="enum class in com.here.sdk.mapview">TranslucentMapLayerGroup.ErrorCode</a></td>
  <td><div class="block">
  Error codes for creating the group.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-errordetails"
  title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.ErrorDetails</a></td>
  <td><div class="block">
  Describes the reason for failing to create the group.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception"
  title="class in com.here.sdk.mapview">TranslucentMapLayerGroup.InstantiationException</a></td>
  <td><div class="block">
  Thrown when failing to build the group.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-trianglemeshbuilder"
  title="class in com.here.sdk.mapview">TriangleMeshBuilder</a></td>
  <td><div class="block">
  Builder for a single triangle.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-visibilitystate"
  title="enum class in com.here.sdk.mapview">VisibilityState</a></td>
  <td><div class="block">
  Represents the visibility state of an SDK map view's object.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-watermarkstyle"
  title="enum class in com.here.sdk.mapview">WatermarkStyle</a></td>
  <td><div class="block">
  Defines the style of the HERE watermark logo.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

</div>


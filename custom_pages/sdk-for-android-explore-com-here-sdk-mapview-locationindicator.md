---
title: "LocationIndicator (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-locationindicator"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.LocationIndicator →
com.here.NativeBase → com.here.sdk.mapview.LocationIndicator

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">LocationIndicator</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Graphical object to represent the location of the user on the map. It is
either a green dot for pedestrian style or a triangular arrow for
vehicle navigation style. This style can be changed by
setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)
The location is made available to an instance of this class by calling
updateLocation(Location) or updateLocation(Location, MapCameraUpdate) .
Use enable(com.here.sdk.mapview.MapViewBase) to add this object to the
map and disable() to remove it. Take care that the location indicator is
not accidentally added to the map view multiple times for example when
the android activity is recreated after an orientation change. Note: The
LocationIndicator is always rendered at a fixed altitude near 0.
Changing the MapCamera to look at geographic coordinates with an
altitude that is higher can cause the following behavior: If the
MapCamera angle is tilted and altitude is too high, the
LocationIndicator can unexpectedly disappear from the viewport due to
the new perspective.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-locationindicator-indicatorstyle"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>LocationIndicator.IndicatorStyle</code></a></td>
  <td><div class="block">
  The predefined styles for the location indicator which are pedestrian
  and navigation mode.
  </div></td>
  </tr>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-locationindicator-markertype"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>LocationIndicator.MarkerType</code></a></td>
  <td><div class="block">
  Enum to identify different types of markers of the location indicator.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>LocationIndicator()</code></pre></td>
  <td><div class="block">
  Creates an instance of LocationIndicator.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>LocationIndicator(MapViewBase mapView)</code></pre></td>
  <td><div class="block">
  Creates an instance of LocationIndicator and adds it to provided
  MapViewBase .
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods
  Deprecated Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>disable()</code></pre></td>
  <td><div class="block">
  This function removes LocationIndicator from map view.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>enable(MapViewBase mapView)</code></pre></td>
  <td><div class="block">
  Enables LocationIndicator for provided MapViewBase .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-color"
  title="class in com.here.sdk.core"><code>Color</code></a></td>
  <td><pre><code>getHaloColor(LocationIndicator.IndicatorStyle style)</code></pre></td>
  <td><div class="block">
  Retrieves the color of the accuracy indicator halo for the requested
  IndicatorStyle.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-locationindicator-indicatorstyle"
  title="enum class in com.here.sdk.mapview"><code>LocationIndicator.IndicatorStyle</code></a></td>
  <td><pre><code>getLocationIndicatorStyle()</code></pre></td>
  <td><div class="block">
  Returns visual style of location indicator.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-materialreflectivity"
  title="class in com.here.sdk.mapview"><code>MaterialReflectivity</code></a></td>
  <td><pre><code>getMaterialReflectivity()</code></pre></td>
  <td><div class="block">
  Retrieves the material reflectivity applied to all markers of location
  indicator.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><pre><code>getOpacity()</code></pre></td>
  <td><div class="block">
  Gets the current opacity of the location indicator.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isAccuracyVisualized()</code></pre></td>
  <td><div class="block">
  Returns whether Location.horizontalAccuracyInMeters is used to scale the
  accuracy indicator halo.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isActive()</code></pre></td>
  <td><div class="block">
  Returns true if active version of the location indicator is shown or
  false when inactive version is shown.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setAccuracyVisualized(boolean value)</code></pre></td>
  <td><div class="block">
  Sets whether Location.horizontalAccuracyInMeters is used to scale the
  accuracy indicator halo.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setActive(boolean value)</code></pre></td>
  <td><div class="block">
  Sets whether the active or inactive version of location indicator is to
  be shown.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setHaloColor(LocationIndicator.IndicatorStyle style,
   Color color)</code></pre></td>
  <td><div class="block">
  Sets the color of the accuracy indicator halo for a given style.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setLocationIndicatorStyle(LocationIndicator.IndicatorStyle value)</code></pre></td>
  <td><div class="block">
  Sets the visual style of location indicator.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setMarker3dModel(MapMarker3DModel model,
   double scale,
   LocationIndicator.MarkerType type)</code></pre></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.27.0.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setMarker3dModel(MapMarker3DModel model,
   double scale,
   LocationIndicator.MarkerType type,
   RenderSize.Unit renderSizeUnit)</code></pre></td>
  <td><div class="block">
  Sets the MapMarker3DModel asset to be displayed as location indicator
  for a specified type.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setMaterialReflectivity(MaterialReflectivity value)</code></pre></td>
  <td><div class="block">
  Sets the material reflectivity properties for all markers of location
  indicator including its halo.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setOpacity(double value)</code></pre></td>
  <td><div class="block">
  Sets the opacity of the location indicator.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>updateLocation(Location location)</code></pre></td>
  <td><div class="block">
  Updates the indicator to a new location.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>updateLocation(Location location,
   MapCameraUpdate cameraUpdate)</code></pre></td>
  <td><div class="block">
  Updates the indicator to a new location and applies a camera update at
  the same time.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### LocationIndicator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationIndicator</span>()

    </div>

    <div class="block">

    Creates an instance of LocationIndicator.

    </div>

    </div>

  - <div id="<init>(com.here.sdk.mapview.MapViewBase)"
    class="section detail">

    ### LocationIndicator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationIndicator</span><span class="parameters">(@NonNull
    [MapViewBase](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview") mapView)</span>

    </div>

    <div class="block">

    Creates an instance of LocationIndicator and adds it to provided
    MapViewBase .

    </div>

    Parameters:  
    `mapView` -

    The
    [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")
    instance.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="enable(com.here.sdk.mapview.MapViewBase)"
    class="section detail">

    ### enable

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enable</span><span class="parameters">(@NonNull
    [MapViewBase](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview") mapView)</span>

    </div>

    <div class="block">

    Enables LocationIndicator for provided MapViewBase . If
    LocationIndicator is already enabled (added to map view) for passed
    map view, this function does nothing. If LocationIndicator is added
    to different MapViewBase , this function removes first
    LocationIndicator from previous map view before adding to new one.

    </div>

    Parameters:  
    `mapView` -

    The
    [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")
    instance.

    </div>

  - <div id="disable()" class="section detail">

    ### disable

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disable</span>()

    </div>

    <div class="block">

    This function removes LocationIndicator from map view. If
    LocationIndicator was not added to any map view yet, this function
    does nothing.

    </div>

    </div>

  - <div id="updateLocation(com.here.sdk.core.Location)"
    class="section detail">

    ### updateLocation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateLocation</span><span class="parameters">(@NonNull
    [Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core") location)</span>

    </div>

    <div class="block">

    Updates the indicator to a new location. If accuracy visualized is
    set to true the field Location.horizontalAccuracyInMeters determines
    the size of the accuracy indicator halo. The altitude of the
    location is ignored.

    </div>

    Parameters:  
    `location` -

    The updated location of the user.

    </div>

  - <div id="updateLocation(com.here.sdk.core.Location,com.here.sdk.mapview.MapCameraUpdate)"
    class="section detail">

    ### updateLocation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateLocation</span><span class="parameters">(@NonNull
    [Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core") location,
    @NonNull
    [MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview") cameraUpdate)</span>

    </div>

    <div class="block">

    Updates the indicator to a new location and applies a camera update
    at the same time. Does nothing if the indicator instance is not
    enabled. If accuracy visualized is set to true the field
    Location.horizontalAccuracyInMeters determines the size of the
    accuracy indicator halo. The altitude of the location is ignored.

    </div>

    Parameters:  
    `location` -

    The updated location of the user.

    `cameraUpdate` -

    The update to apply to the camera.

    </div>

  - <div id="setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType)"
    class="section detail">

    ### setMarker3dModel

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a>
    </span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMarker3dModel</span><span class="parameters">(@NonNull
    [MapMarker3DModel](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel "class in com.here.sdk.mapview") model,
    double scale, @NonNull
    [LocationIndicator.MarkerType](sdk-for-android-explore-com-here-sdk-mapview-locationindicator-markertype "enum class in com.here.sdk.mapview") type)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.27.0. Please use the overloaded method with
    [`RenderSize.Unit`](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview")
    instead.

    </div>

    </div>

    <div class="block">

    Sets the MapMarker3DModel asset to be displayed as location
    indicator for a specified type. The 3D model should be oriented with
    y axis up and thus standing on the x/z plane where the z axis is the
    depth. The direction in which the location indicator is pointing is
    the positive z axis. Please note that only MapMarker3DModel created
    from \*.obj files are supported. Models created from Mesh will be
    ignored.

    </div>

    Parameters:  
    `model` -

    The MapMarker3DModel object to be displayed for the specified type.
    Only models created from obj files are supported. Those created from
    mesh will be ignored.

    `scale` -

    The scaling which will be applied to the marker model. As the size
    of the location marker should be aligned on devices with different
    resolutions the scale factor is applied relative to the ppi value
    and thus differs from the scale which is passed to
    [`MapMarker3D`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d "class in com.here.sdk.mapview")
    objects. Meter is used for the unit of the map marker 3d model
    coordinate system. For historical reason, the scale factor is
    internally devided by 6. To display a unit qube of 1x1x1 meter as
    is, please use a scale value of 6.0.

    `type` -

    The type of location marker for which the marker 3d model should be
    replaced.

    </div>

  - <div id="setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType,com.here.sdk.mapview.RenderSize.Unit)"
    class="section detail">

    ### setMarker3dModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMarker3dModel</span><span class="parameters">(@NonNull
    [MapMarker3DModel](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel "class in com.here.sdk.mapview") model,
    double scale, @NonNull
    [LocationIndicator.MarkerType](sdk-for-android-explore-com-here-sdk-mapview-locationindicator-markertype "enum class in com.here.sdk.mapview") type,
    @NonNull
    [RenderSize.Unit](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview") renderSizeUnit)</span>

    </div>

    <div class="block">

    Sets the MapMarker3DModel asset to be displayed as location
    indicator for a specified type. The 3D model should be oriented with
    y axis up and thus standing on the x/z plane where the z axis is the
    depth. The direction in which the location indicator is pointing is
    the positive z axis. Please note that only MapMarker3DModel created
    from obj files are supported. Models created from Mesh will be
    ignored.

    </div>

    Parameters:  
    `model` -

    The
    [`MapMarker3DModel`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel "class in com.here.sdk.mapview")
    object to be displayed for the specified type. Only models created
    from `obj` files are supported. Those created from mesh will be
    ignored.

    `scale` -

    A scale factor applied to the marker model.

    `type` -

    The type of location marker for which the marker 3d model should be
    replaced.

    `renderSizeUnit` -

    The
    [`RenderSize.Unit`](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview")
    specifying how the vertex coordinates of the 3D model are being
    interpreted. It specifies whether the 3D model is placed in world or
    screen coordinate space.
    [`RenderSize.Unit.METERS`](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit#METERS)
    will make the 3D model use world coordinate space, meaning that it
    will change size together with the map when it is zoomed in and out.
    A simple 10 by 10 by 10 (in model space) cube will have a size of 10
    by 10 by 10 meters in world space.
    [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit#PIXELS)
    makes the 3D model use screen coordinate space, meaning that it will
    have constant size on the screen regardless of how the map zoom
    changes. A simple 10 by 10 (in model space) rectangle will have a
    size of 10 by 10 pixels on the screen.
    [`RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS`](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit#DENSITY_INDEPENDENT_PIXELS)
    is similar to pixels, but the resulting size will take into account
    the pixel density of the display, meaning that physical size on the
    screen will be approximately the same regardless of the size or
    resolution of the display.

    </div>

  - <div id="setHaloColor(com.here.sdk.mapview.LocationIndicator.IndicatorStyle,com.here.sdk.core.Color)"
    class="section detail">

    ### setHaloColor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHaloColor</span><span class="parameters">(@NonNull
    [LocationIndicator.IndicatorStyle](sdk-for-android-explore-com-here-sdk-mapview-locationindicator-indicatorstyle "enum class in com.here.sdk.mapview") style,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") color)</span>

    </div>

    <div class="block">

    Sets the color of the accuracy indicator halo for a given style.

    </div>

    Parameters:  
    `style` -

    The type of IndicatorStyle for which the color should be assigned.

    `color` -

    The color to be applied to the halo for a specified IndicatorStyle.
    Note: This is a beta release of this feature, so there could be a
    few bugs and unexpected behaviors. Related APIs may change for new
    releases without a deprecation process.

    </div>

  - <div id="getHaloColor(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)"
    class="section detail">

    ### getHaloColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getHaloColor</span><span class="parameters">(@NonNull
    [LocationIndicator.IndicatorStyle](sdk-for-android-explore-com-here-sdk-mapview-locationindicator-indicatorstyle "enum class in com.here.sdk.mapview") style)</span>

    </div>

    <div class="block">

    Retrieves the color of the accuracy indicator halo for the requested
    IndicatorStyle. The default color is a translucent turquoise
    (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.

    </div>

    Parameters:  
    `style` -

    The type of IndicatorStyle for which the color should be returned.

    Returns:  
    The color of the halo for the specified IndicatorStyle. Note: This
    is a beta release of this feature, so there could be a few bugs and
    unexpected behaviors. Related APIs may change for new releases
    without a deprecation process.

    </div>

  - <div id="isAccuracyVisualized()" class="section detail">

    ### isAccuracyVisualized

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAccuracyVisualized</span>()

    </div>

    <div class="block">

    Returns whether Location.horizontalAccuracyInMeters is used to scale
    the accuracy indicator halo. Default is false , in which case the
    halo has a fixed and zoom level independent size.

    </div>

    Returns:  
    Whether the horizontal accuracy is visualized by scaling the
    accuracy indicator halo.

    </div>

  - <div id="setAccuracyVisualized(boolean)" class="section detail">

    ### setAccuracyVisualized

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAccuracyVisualized</span><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether Location.horizontalAccuracyInMeters is used to scale
    the accuracy indicator halo. Default is false , in which case the
    halo has a fixed and zoom level independent size. When set to true ,
    the radius of the halo corresponds to the value of
    Location.horizontalAccuracyInMeters passed to
    updateLocation(Location) and scales in world coordinates. For values
    smaller than 20 meters the halo is hidden. The radius of the halo is
    limited to 500 meters and values higher than that or null will keep
    the halo at that size. If the location indicator is set to inactive
    (which can be checked via isActive() flag), then the halo is always
    hidden. The value of this property remains unchanged regardless of
    the flag's value. If the location indicator is set to active:
    Built-in location indicators: The halo is always shown. If the
    accuracy visualization is set to true , the size of the halo scales
    with Location.horizontalAccuracyInMeters in world coordinates. If
    the accuracy visualization is set to false , halo displays at a
    default size. Custom location indicator: If the accuracy
    visualization is set to true , halo is shown and the size of the
    halo scales with Location.horizontalAccuracyInMeters in world
    coordinates. If the accuracy visualization is set to false , no halo
    is shown since it might not fit together with the custom 3d model.

    </div>

    Parameters:  
    `value` -

    Whether the horizontal accuracy is visualized by scaling the
    accuracy indicator halo.

    </div>

  - <div id="getLocationIndicatorStyle()" class="section detail">

    ### getLocationIndicatorStyle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LocationIndicator.IndicatorStyle](sdk-for-android-explore-com-here-sdk-mapview-locationindicator-indicatorstyle "enum class in com.here.sdk.mapview")</span> <span class="element-name">getLocationIndicatorStyle</span>()

    </div>

    <div class="block">

    Returns visual style of location indicator. By default, it is set to
    LocationIndicator.IndicatorStyle.NAVIGATION .

    </div>

    Returns:  
    The visual style of location indicator.

    </div>

  - <div id="setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)"
    class="section detail">

    ### setLocationIndicatorStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLocationIndicatorStyle</span><span class="parameters">(@NonNull
    [LocationIndicator.IndicatorStyle](sdk-for-android-explore-com-here-sdk-mapview-locationindicator-indicatorstyle "enum class in com.here.sdk.mapview") value)</span>

    </div>

    <div class="block">

    Sets the visual style of location indicator. By default, it is set
    to LocationIndicator.IndicatorStyle.NAVIGATION .

    </div>

    Parameters:  
    `value` -

    The visual style of location indicator.

    </div>

  - <div id="isActive()" class="section detail">

    ### isActive

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isActive</span>()

    </div>

    <div class="block">

    Returns true if active version of the location indicator is shown or
    false when inactive version is shown. By default, it is true .

    </div>

    Returns:  
    A Boolean value that determines whether the active on inactive
    version of location indicator is shown.

    </div>

  - <div id="setActive(boolean)" class="section detail">

    ### setActive

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActive</span><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether the active or inactive version of location indicator is
    to be shown. the indicator to active state if true is passed and to
    inactive state when false is passed. By default, it is true .

    </div>

    Parameters:  
    `value` -

    A Boolean value that determines whether the active on inactive
    version of location indicator is shown.

    </div>

  - <div id="getOpacity()" class="section detail">

    ### getOpacity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOpacity</span>()

    </div>

    <div class="block">

    Gets the current opacity of the location indicator. Default value is
    1.0 which means location indicator is displayed with the default
    alpha channel of the texture.

    </div>

    Returns:  
    The factor applied to the alpha channel of both the location
    indicator's texture and the accuracy indicator's halo color.

    </div>

  - <div id="setOpacity(double)" class="section detail">

    ### setOpacity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpacity</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the opacity of the location indicator. Provided value is
    clamped in range \[0.0, 1.0\]. Default value is 1.0 which means
    location indicator is displayed with the default alpha channel of
    the texture.

    </div>

    Parameters:  
    `value` -

    The factor applied to the alpha channel of both the location
    indicator's texture and the accuracy indicator's halo color.

    </div>

  - <div id="getMaterialReflectivity()" class="section detail">

    ### getMaterialReflectivity

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[MaterialReflectivity](sdk-for-android-explore-com-here-sdk-mapview-materialreflectivity "class in com.here.sdk.mapview")</span> <span class="element-name">getMaterialReflectivity</span>()

    </div>

    <div class="block">

    Retrieves the material reflectivity applied to all markers of
    location indicator. Note: This is a beta release of this feature, so
    there could be a few bugs and unexpected behaviors. Related APIs may
    change for new releases without a deprecation process. Enables
    per‑pixel lighting for all internal markers (navigation, pedestrian,
    inactive variants) and the halo when assigned. While
    materialReflectivity is non‑null the markers are shaded by scene
    lights using the provided ambient / diffuse factors. When set back
    to null , lighting is disabled and markers revert to unlit
    (emissive) rendering. Default value is null .

    </div>

    Returns:  
    The material reflectivity properties of the location indicator.

    </div>

  - <div id="setMaterialReflectivity(com.here.sdk.mapview.MaterialReflectivity)"
    class="section detail">

    ### setMaterialReflectivity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMaterialReflectivity</span><span class="parameters">(@Nullable
    [MaterialReflectivity](sdk-for-android-explore-com-here-sdk-mapview-materialreflectivity "class in com.here.sdk.mapview") value)</span>

    </div>

    <div class="block">

    Sets the material reflectivity properties for all markers of
    location indicator including its halo. This value affects also any
    custom markers set with setMarker3dModel . Enables per‑pixel
    lighting for all internal markers (navigation, pedestrian, inactive
    variants) and the halo when assigned. While materialReflectivity is
    non‑null the markers are shaded by scene lights using the provided
    ambient / diffuse factors. When set back to null , lighting is
    disabled and markers revert to unlit (emissive) rendering. Default
    value is null .

    </div>

    Parameters:  
    `value` -

    The material reflectivity properties of the location indicator.

    </div>

  </div>

</div>


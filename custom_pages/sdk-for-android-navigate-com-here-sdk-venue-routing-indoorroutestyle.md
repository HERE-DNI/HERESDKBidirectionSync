---
title: "IndoorRouteStyle (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-package-summary">com.here.sdk.venue.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.venue.routing.IndoorRouteStyle → com.here.NativeBase com.here.sdk.venue.routing.IndoorRouteStyle → com.here.sdk.venue.routing.IndoorRouteStyle

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">IndoorRouteStyle</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Represents a style of the indoor route. Contains information about route colors and widths. Optionally, this style allows to set MapMarker instances that can be used for specific route elements.

</div>

</div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      IndoorRouteStyle ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDestinationMarker ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The destination map marker of the resulting route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDriveMarker ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The drive map marker of the resulting route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getIndoorMarkerFor ( IndoorLevelChangeFeatures feature,
       int deltaZ)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a MapMarker for a given indoor feature and the number of levels to change.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">`Color`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getIndoorPolylineColor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The color of polylines for indoor route sections.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getIndoorPolylineWidth ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The width in pixels of polylines for indoor route sections.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getStartMarker ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The start map marker of the resulting route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWalkMarker ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The walk map marker of the resulting route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDestinationMarker ( MapMarker value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The destination map marker of the resulting route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDriveMarker ( MapMarker value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The drive map marker of the resulting route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setIndoorMarkersFor ( IndoorLevelChangeFeatures feature, MapMarker upMarker, MapMarker downMarker, MapMarker exitMarker)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets map markers for the given indoor feature.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setIndoorPolylineColor ( Color value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The color of polylines for indoor route sections.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setIndoorPolylineWidth (double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The width in pixels of polylines for indoor route sections.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setStartMarker ( MapMarker value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The start map marker of the resulting route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setWalkMarker ( MapMarker value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The walk map marker of the resulting route.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### IndoorRouteStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IndoorRouteStyle</span>()

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getIndoorMarkerFor-com-here-sdk-routing-IndoorLevelChangeFeatures-int" class="section detail">

    ### getIndoorMarkerFor

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getIndoorMarkerFor</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a> feature, int deltaZ)</span>

    </div>

    <div class="block">

    Returns a MapMarker for a given indoor feature and the number of levels to change. By default, no map markers are provided.

    </div>

    Parameters:  
    `feature` -

    An indoor feature.

    `deltaZ` -

    A number of levels to change, positive for up, negative for down. In the case of 0, the method returns an exit map marker.

    Returns:  
    The result <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a>, if it was set.

    </div>

  - <div id="sdk-for-android-navigate-setIndoorMarkersFor-com-here-sdk-routing-IndoorLevelChangeFeatures-com-here-sdk-mapview-MapMarker-com-here-sdk-mapview-MapMarker-com-here-sdk-mapview-MapMarker" class="section detail">

    ### setIndoorMarkersFor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndoorMarkersFor</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a> feature, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> upMarker, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> downMarker, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> exitMarker)</span>

    </div>

    <div class="block">

    Sets map markers for the given indoor feature.

    </div>

    Parameters:  
    `feature` -

    An indoor feature.

    `upMarker` -

    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> to go up.

    `downMarker` -

    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> to go down.

    `exitMarker` -

    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> to exit the indoor feature.

    </div>

  - <div id="sdk-for-android-navigate-getIndoorPolylineWidth" class="section detail">

    ### getIndoorPolylineWidth

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getIndoorPolylineWidth</span>()

    </div>

    <div class="block">

    The width in pixels of polylines for indoor route sections.

    </div>

    Returns:  
    The width in pixels. Default value is 15 pixels

    </div>

  - <div id="sdk-for-android-navigate-setIndoorPolylineWidth-double" class="section detail">

    ### setIndoorPolylineWidth

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndoorPolylineWidth</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    The width in pixels of polylines for indoor route sections.

    </div>

    Parameters:  
    `value` -

    The width in pixels. Default value is 15 pixels

    </div>

  - <div id="sdk-for-android-navigate-getIndoorPolylineColor" class="section detail">

    ### getIndoorPolylineColor

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getIndoorPolylineColor</span>()

    </div>

    <div class="block">

    The color of polylines for indoor route sections.

    </div>

    Returns:  
    The color value. The default color is #48DAD0.

    </div>

  - <div id="sdk-for-android-navigate-setIndoorPolylineColor-com-here-sdk-core-Color" class="section detail">

    ### setIndoorPolylineColor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndoorPolylineColor</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span>

    </div>

    <div class="block">

    The color of polylines for indoor route sections.

    </div>

    Parameters:  
    `value` -

    The color value. The default color is #48DAD0.

    </div>

  - <div id="sdk-for-android-navigate-getStartMarker" class="section detail">

    ### getStartMarker

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getStartMarker</span>()

    </div>

    <div class="block">

    The start map marker of the resulting route.

    </div>

    Returns:  
    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> instance representing the start of the route. By default, no map marker is provided.

    </div>

  - <div id="sdk-for-android-navigate-setStartMarker-com-here-sdk-mapview-MapMarker" class="section detail">

    ### setStartMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStartMarker</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span>

    </div>

    <div class="block">

    The start map marker of the resulting route.

    </div>

    Parameters:  
    `value` -

    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> instance representing the start of the route. By default, no map marker is provided.

    </div>

  - <div id="sdk-for-android-navigate-getDestinationMarker" class="section detail">

    ### getDestinationMarker

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getDestinationMarker</span>()

    </div>

    <div class="block">

    The destination map marker of the resulting route.

    </div>

    Returns:  
    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> instance representing the destination of the route. By default, no map marker is provided

    </div>

  - <div id="sdk-for-android-navigate-setDestinationMarker-com-here-sdk-mapview-MapMarker" class="section detail">

    ### setDestinationMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDestinationMarker</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span>

    </div>

    <div class="block">

    The destination map marker of the resulting route.

    </div>

    Parameters:  
    `value` -

    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> instance representing the destination of the route. By default, no map marker is provided

    </div>

  - <div id="sdk-for-android-navigate-getWalkMarker" class="section detail">

    ### getWalkMarker

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getWalkMarker</span>()

    </div>

    <div class="block">

    The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.

    </div>

    Returns:  
    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> instance representing the walk point of the route. By default, no map marker is provided.

    </div>

  - <div id="sdk-for-android-navigate-setWalkMarker-com-here-sdk-mapview-MapMarker" class="section detail">

    ### setWalkMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWalkMarker</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span>

    </div>

    <div class="block">

    The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.

    </div>

    Parameters:  
    `value` -

    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> instance representing the walk point of the route. By default, no map marker is provided.

    </div>

  - <div id="sdk-for-android-navigate-getDriveMarker" class="section detail">

    ### getDriveMarker

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getDriveMarker</span>()

    </div>

    <div class="block">

    The drive map marker of the resulting route. It signals that a user should take a transport vehicle.

    </div>

    Returns:  
    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> instance representing the drive point of the route. By default, no map marker is provided.

    </div>

  - <div id="sdk-for-android-navigate-setDriveMarker-com-here-sdk-mapview-MapMarker" class="section detail">

    ### setDriveMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDriveMarker</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span>

    </div>

    <div class="block">

    The drive map marker of the resulting route. It signals that a user should take a transport vehicle.

    </div>

    Parameters:  
    `value` -

    A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a> instance representing the drive point of the route. By default, no map marker is provided.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


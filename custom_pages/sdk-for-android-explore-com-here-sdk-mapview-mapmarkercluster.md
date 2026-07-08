---
title: "MapMarkerCluster (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase
com.here.sdk.mapview.MapMarkerCluster → com.here.NativeBase
com.here.sdk.mapview.MapMarkerCluster →
com.here.sdk.mapview.MapMarkerCluster

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapMarkerCluster</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Groups map markers and enables their clustering to reduce visual clutter
when there are many of them in a small area. The markers that are close
to each other are replaced by a single cluster marker. Cluster groups
are generated based on geographical distance between objects, not based
on screen space collision. Hence it is possible, that cluster markers
can overlap. The markers can be added to a cluster or to a scene, but
not to both. To display the cluster on the map, add it to the scene
using
MapScene.addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster) .
The display of a cluster is only guaranteed in case its origin is within
the viewport. At the moment, this is a known limitation that mostly
affects clusters which are visually large and cover a sizeable part of
the viewport. Markers part of the cluster with opacity set to zero are
still on the map and are considered for picking and clustering.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapMarkerCluster.CounterStyle</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Styling options for a marker cluster which is represented by the
  marker count as a text.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapMarkerCluster.Grouping</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Represents a group of map markers belonging to a cluster.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-imagestyle"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapMarkerCluster.ImageStyle</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This class specifies the visual appearance of a cluster marker.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      MapMarkerCluster ( MapMarkerCluster.ImageStyle imageStyle)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of a map marker cluster which is represented as
  an image.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMarkerCluster ( MapMarkerCluster.ImageStyle imageStyle, MapMarkerCluster.CounterStyle counterStyle)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of a map marker cluster which is represented as
  an image along with a counter showing how many markers are actually
  grouped under particular cluster icon.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addMapMarker ( MapMarker marker)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a map marker to this cluster.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addMapMarkers ( List < MapMarker > markers)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a list of map markers to this cluster.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`MapMarker`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMarkers ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the list of map markers which currently belong to this
  cluster.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOpacity ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current opacity of the marker cluster image.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeAllMapMarkers ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes all map markers from this cluster.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeMapMarker ( MapMarker marker)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a map marker from this cluster.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeMapMarkers ( List < MapMarker > markers)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a list of map markers from this cluster.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOpacity (double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the opacity of the marker cluster image.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-mapview-MapMarkerCluster-ImageStyle"
    class="section detail">

    ### MapMarkerCluster

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarkerCluster</span><span class="parameters">(@NonNull
    [MapMarkerCluster.ImageStyle](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-imagestyle "class in com.here.sdk.mapview") imageStyle)</span>

    </div>

    <div class="block">

    Creates a new instance of a map marker cluster which is represented
    as an image. Any modification to object passed as imageStyle after
    creation of MapMarkerCluster does not have any effect.

    </div>

    Parameters:  
    `imageStyle` -

    The visual representation for the cluster.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-mapview-MapMarkerCluster-ImageStyle-com-here-sdk-mapview-MapMarkerCluster-CounterStyle"
    class="section detail">

    ### MapMarkerCluster

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarkerCluster</span><span class="parameters">(@NonNull
    [MapMarkerCluster.ImageStyle](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-imagestyle "class in com.here.sdk.mapview") imageStyle,
    @NonNull
    [MapMarkerCluster.CounterStyle](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle "class in com.here.sdk.mapview") counterStyle)</span>

    </div>

    <div class="block">

    Creates a new instance of a map marker cluster which is represented
    as an image along with a counter showing how many markers are
    actually grouped under particular cluster icon. Any modification to
    imageStyle or counterStyle after creation of MapMarkerCluster does
    not have any effect.

    </div>

    Parameters:  
    `imageStyle` -

    Describes the visual appearance of cluster icon.

    `counterStyle` -

    Describes the appearance of marker count label.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-addMapMarker-com-here-sdk-mapview-MapMarker"
    class="section detail">

    ### addMapMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarker</span><span class="parameters">(@NonNull
    [MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview") marker)</span>

    </div>

    <div class="block">

    Adds a map marker to this cluster. Adding a marker which is already
    part of the cluster or which was already added to the map scene has
    no effect.

    </div>

    Parameters:  
    `marker` -

    The marker.

    </div>

  - <div id="sdk-for-android-explore-addMapMarkers-java-util-List"
    class="section detail">

    ### addMapMarkers

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarkers</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")\> markers)</span>

    </div>

    <div class="block">

    Adds a list of map markers to this cluster. Markers which are
    already part of the cluster or which were already added to the map
    scene will be ignored.

    </div>

    Parameters:  
    `markers` -

    The list of markers.

    </div>

  - <div id="sdk-for-android-explore-removeMapMarker-com-here-sdk-mapview-MapMarker"
    class="section detail">

    ### removeMapMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarker</span><span class="parameters">(@NonNull
    [MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview") marker)</span>

    </div>

    <div class="block">

    Removes a map marker from this cluster. Removing a marker which is
    not part of this cluster has no effect.

    </div>

    Parameters:  
    `marker` -

    The marker.

    </div>

  - <div id="sdk-for-android-explore-removeMapMarkers-java-util-List"
    class="section detail">

    ### removeMapMarkers

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarkers</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")\> markers)</span>

    </div>

    <div class="block">

    Removes a list of map markers from this cluster. Removing markers
    which are not part of this cluster has no effect.

    </div>

    Parameters:  
    `markers` -

    The list of markers.

    </div>

  - <div id="sdk-for-android-explore-removeAllMapMarkers"
    class="section detail">

    ### removeAllMapMarkers

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapMarkers</span>()

    </div>

    <div class="block">

    Removes all map markers from this cluster.

    </div>

    </div>

  - <div id="sdk-for-android-explore-getMarkers" class="section detail">

    ### getMarkers

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")\></span> <span class="element-name">getMarkers</span>()

    </div>

    <div class="block">

    Returns the list of map markers which currently belong to this
    cluster. Modifying the list has no effect on the marker cluster.

    </div>

    Returns:  
    The list of map markers which currently belong to this cluster.

    </div>

  - <div id="sdk-for-android-explore-getOpacity" class="section detail">

    ### getOpacity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOpacity</span>()

    </div>

    <div class="block">

    Gets the current opacity of the marker cluster image.

    </div>

    Returns:  
    Opacity is the factor which is applied to the alpha channel of the
    image used for marker cluster.

    </div>

  - <div id="sdk-for-android-explore-setOpacity-double"
    class="section detail">

    ### setOpacity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpacity</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the opacity of the marker cluster image. Provided value is
    clamped in range \[0.0, 1.0\]. Default value is 1.0 which means
    marker cluster is displayed with the default opacity of the image.
    Marker clusters with opacity value set to 0.0 are still on the map
    and are considered for picking. Markers part of cluster will use
    their respective opacity when not displayed as a cluster icon.

    </div>

    Parameters:  
    `value` -

    Opacity is the factor which is applied to the alpha channel of the
    image used for marker cluster.

    </div>

  </div>


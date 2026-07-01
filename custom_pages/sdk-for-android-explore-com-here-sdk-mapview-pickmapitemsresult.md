---
title: "PickMapItemsResult (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-pickmapitemsresult"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.PickMapItemsResult →
com.here.NativeBase → com.here.sdk.mapview.PickMapItemsResult

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">PickMapItemsResult</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Carries results from the picking of map items on the map scene.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping"
  title="class in com.here.sdk.mapview"><code>MapMarkerCluster.Grouping</code></a><code>&gt;</code></td>
  <td><pre><code>getClusteredMarkers()</code></pre></td>
  <td><div class="block">
  Gets list of clustered marker groups at the location of picking.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker"
  title="class in com.here.sdk.mapview"><code>MapMarker</code></a><code>&gt;</code></td>
  <td><pre><code>getMarkers()</code></pre></td>
  <td><div class="block">
  Gets list of markers at the location of picking.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d"
  title="class in com.here.sdk.mapview"><code>MapMarker3D</code></a><code>&gt;</code></td>
  <td><pre><code>getMarkers3d()</code></pre></td>
  <td><div class="block">
  Gets list of 3d markers at the location of picking.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolygon"
  title="class in com.here.sdk.mapview"><code>MapPolygon</code></a><code>&gt;</code></td>
  <td><pre><code>getPolygons()</code></pre></td>
  <td><div class="block">
  Gets list of polygons at the location of picking.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline"
  title="class in com.here.sdk.mapview"><code>MapPolyline</code></a><code>&gt;</code></td>
  <td><pre><code>getPolylines()</code></pre></td>
  <td><div class="block">
  Gets list of polylines at the location of picking.
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

- <div id="method-detail" class="section method-details">

  - <div id="getClusteredMarkers()" class="section detail">

    ### getClusteredMarkers

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarkerCluster.Grouping](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping "class in com.here.sdk.mapview")></span> <span class="element-name">getClusteredMarkers</span>()

    </div>

    <div class="block">

    Gets list of clustered marker groups at the location of picking.

    </div>

    Returns:  
    List of marker groups (represented by a single cluster marker) or
    individual markers belonging to a cluster at the location of
    picking.

    </div>

  - <div id="getMarkers()" class="section detail">

    ### getMarkers

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")></span> <span class="element-name">getMarkers</span>()

    </div>

    <div class="block">

    Gets list of markers at the location of picking.

    </div>

    Returns:  
    List of markers at the location of picking.

    </div>

  - <div id="getMarkers3d()" class="section detail">

    ### getMarkers3d

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarker3D](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d "class in com.here.sdk.mapview")></span> <span class="element-name">getMarkers3d</span>()

    </div>

    <div class="block">

    Gets list of 3d markers at the location of picking.

    </div>

    Returns:  
    List of 3d markers at the location of picking.

    </div>

  - <div id="getPolylines()" class="section detail">

    ### getPolylines

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview")></span> <span class="element-name">getPolylines</span>()

    </div>

    <div class="block">

    Gets list of polylines at the location of picking.

    </div>

    Returns:  
    List of polylines at the location of picking.

    </div>

  - <div id="getPolygons()" class="section detail">

    ### getPolygons

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapPolygon](sdk-for-android-explore-com-here-sdk-mapview-mappolygon "class in com.here.sdk.mapview")></span> <span class="element-name">getPolygons</span>()

    </div>

    <div class="block">

    Gets list of polygons at the location of picking.

    </div>

    Returns:  
    List of polygons at the location of picking.

    </div>

  </div>

</div>


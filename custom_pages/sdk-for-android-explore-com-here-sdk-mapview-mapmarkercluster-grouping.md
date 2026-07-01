---
title: "MapMarkerCluster.Grouping (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.MapMarkerCluster.Grouping

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapMarkerCluster](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapMarkerCluster.Grouping</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a group of map markers belonging to a cluster. It contains a
list of map markers grouped on map view under single icon of marker
cluster or single map marker entry for markers being part of cluster but
spread enough not to be grouped.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

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
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker"
  title="class in com.here.sdk.mapview"><code>MapMarker</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping#markers"
  class="member-name-link"><code>markers</code></a></td>
  <td><div class="block">
  List of map markers grouped on map view under map marker cluster icon.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster"
  title="class in com.here.sdk.mapview"><code>MapMarkerCluster</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping#parent"
  class="member-name-link"><code>parent</code></a></td>
  <td><div class="block">
  Map marker cluster that entries in markers belong to.
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
  <td><pre><code>Grouping(List&lt;MapMarker&gt; markers,
   MapMarkerCluster parent)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

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

- <div id="field-detail" class="section field-details">

  - <div id="markers" class="section detail">

    ### markers

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")></span> <span class="element-name">markers</span>

    </div>

    <div class="block">

    List of map markers grouped on map view under map marker cluster
    icon.

    </div>

    </div>

  - <div id="parent" class="section detail">

    ### parent

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMarkerCluster](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster "class in com.here.sdk.mapview")</span> <span class="element-name">parent</span>

    </div>

    <div class="block">

    Map marker cluster that entries in markers belong to.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.util.List,com.here.sdk.mapview.MapMarkerCluster)"
    class="section detail">

    ### Grouping

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Grouping</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")> markers,
    @NonNull
    [MapMarkerCluster](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster "class in com.here.sdk.mapview") parent)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `markers` -

    List of map markers grouped on map view under map marker cluster
    icon.

    `parent` -

    Map marker cluster that entries in
    [`markers`](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping#markers)
    belong to.

    </div>

  </div>

</div>


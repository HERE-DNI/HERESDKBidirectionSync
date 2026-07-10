---
title: "MapMarkerCluster.Grouping (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.MapMarkerCluster.Grouping → com.here.sdk.mapview.MapMarkerCluster.Grouping

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">MapMarkerCluster.Grouping</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a group of map markers belonging to a cluster. It contains a list of map markers grouped on map view under single icon of marker cluster or single map marker entry for markers being part of cluster but spread enough not to be grouped.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">`MapMarker`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping#markers" class="member-name-link"><code>markers</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of map markers grouped on map view under map marker cluster icon.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster" title="class in com.here.sdk.mapview">`MapMarkerCluster`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping#parent" class="member-name-link"><code>parent</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map marker cluster that entries in markers belong to.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      Grouping ( List < MapMarker > markers, MapMarkerCluster parent)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-markers" class="section detail">

    ### markers

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>\></span> <span class="element-name">markers</span>

    </div>

    <div class="block">

    List of map markers grouped on map view under map marker cluster icon.

    </div>

    </div>

  - <div id="sdk-for-android-explore-parent" class="section detail">

    ### parent

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a></span> <span class="element-name">parent</span>

    </div>

    <div class="block">

    Map marker cluster that entries in markers belong to.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-java-util-List-com-here-sdk-mapview-MapMarkerCluster" class="section detail">

    ### Grouping

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Grouping</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>\> markers, @NonNull <a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> parent)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `markers` -

    List of map markers grouped on map view under map marker cluster icon.

    `parent` -

    Map marker cluster that entries in <a href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-grouping#markers">`markers`</a> belong to.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


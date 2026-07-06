---
title: "TileGeoBoundsCalculator (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilegeoboundscalculator"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.TileGeoBoundsCalculator
→ com.here.NativeBase →
com.here.sdk.mapview.datasource.TileGeoBoundsCalculator

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TileGeoBoundsCalculator</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

A calculator of geodetic bounds for tiles identified by keys generated
in a particular tiling scheme ( TilingScheme ). Note: This is a beta
release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation
process.

</div>

</div>

<div class="section summary">

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

      TileGeoBoundsCalculator(TilingScheme tilingScheme)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an instance of TileGeoBoundsCalculator .

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

  [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      boundsOf(TileKey tileKey)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Computes the geodetic bounds (as GeoBox ) for a tile identified by
  TileKey .

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.datasource.TilingScheme)"
    class="section detail">

    ### TileGeoBoundsCalculator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TileGeoBoundsCalculator</span><span class="parameters">(@NonNull
    [TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme)</span>

    </div>

    <div class="block">

    Creates an instance of TileGeoBoundsCalculator .

    </div>

    Parameters:  
    `tilingScheme` -

    The tiling scheme used for generating the tile keys that are to be
    supported by this instance.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-boundsOf(com.here.sdk.mapview.datasource.TileKey)"
    class="section detail">

    ### boundsOf

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">boundsOf</span><span class="parameters">(@NonNull
    [TileKey](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource") tileKey)</span>

    </div>

    <div class="block">

    Computes the geodetic bounds (as GeoBox ) for a tile identified by
    TileKey .

    </div>

    Parameters:  
    `tileKey` -

    [`TileKey`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource")
    to compute geodetic bounds for. The geodetic bounds would be
    calculated relative to the tiling scheme provided at this
    [`TileGeoBoundsCalculator`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilegeoboundscalculator "class in com.here.sdk.mapview.datasource")
    instance creation.

    Returns:  
    The geodetic bounds of tile identified by given
    [`TileKey`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilekey "class in com.here.sdk.mapview.datasource").

    </div>

  </div>

</div>


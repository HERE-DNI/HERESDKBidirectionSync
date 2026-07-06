---
title: "MapLayerMapMeasureDependentStorageLevels (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-maplayermapmeasuredependentstoragelevels"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels
→ com.here.NativeBase →
com.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapLayerMapMeasureDependentStorageLevels</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Provides a mapping between a MapLayer map measure to datasource storage
level.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-method-summary"
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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`MapLayerMapMeasureDependentStorageLevels`](sdk-for-android-explore-com-here-sdk-mapview-maplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      withStorageLevelOffset(int offset)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates an instance of MapLayerMapMeasureDependentStorageLevels with
  the specified storage level offset.

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
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-withStorageLevelOffset(int)"
    class="section detail">

    ### withStorageLevelOffset

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapLayerMapMeasureDependentStorageLevels](sdk-for-android-explore-com-here-sdk-mapview-maplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview")</span> <span class="element-name">withStorageLevelOffset</span><span class="parameters">(int offset)</span>

    </div>

    <div class="block">

    Creates an instance of MapLayerMapMeasureDependentStorageLevels with
    the specified storage level offset. This creates a map where the
    storage level is determined by applying an "offset" to the zoom
    level. A negative offset results in a storage level lower than the
    zoom level, while a positive offset increases it. For example, with
    an offset of 0, the storage level matches the zoom level directly.
    An offset of -1 makes the storage level one less than the zoom
    level, and so on. The offset value is clamped to the range of -3
    to 3. Note: The generated mapping adjusts so that when the map
    camera is significantly tilted, the storage level is further reduced
    for data near the horizon.

    </div>

    Parameters:  
    `offset` -

    Defines an offset of storage level from the zoom level. The value
    will be clamped to a range of -3 to 3.

    Returns:  
    MapLayerMapMeasureDependentStorageLevels instance.

    </div>

  </div>

</div>


---
title: "Region (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-region"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.maploader.Region → com.here.sdk.maploader.Region

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">Region</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Defines an area, especially part of a country or the world that can be downloaded.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader">`Region`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-region#childRegions" class="member-name-link"><code>childRegions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  All child regions for current region.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-region#name" class="member-name-link"><code>name</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Name of region.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-navigabilitytype" title="enum class in com.here.sdk.maploader">`NavigabilityType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-region#navigability" class="member-name-link"><code>navigability</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the navigability type of this region.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">`RegionId`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-region#regionId" class="member-name-link"><code>regionId</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Unique identifier specifying a region.

  </div>

  </div>

  <div class="col-first even-row-color">

  `long`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-region#sizeOnDiskInBytes" class="member-name-link"><code>sizeOnDiskInBytes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `long`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-region#sizeOnNetworkInBytes" class="member-name-link"><code>sizeOnNetworkInBytes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Region size, for downloading/during network operations, in bytes.

  </div>

  </div>

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

      Region ( RegionId regionId)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-regionId" class="section detail">

    ### regionId

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a></span> <span class="element-name">regionId</span>

    </div>

    <div class="block">

    Unique identifier specifying a region.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-name" class="section detail">

    ### name

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">name</span>

    </div>

    <div class="block">

    Name of region. Language is determined by the requested LanguageCode . By default, it is in LanguageCode.EN_US .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-sizeOnDiskInBytes" class="section detail">

    ### sizeOnDiskInBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">sizeOnDiskInBytes</span>

    </div>

    <div class="block">

    Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk. This value is a theoretical maximum for the region's size allocation. Note: If overlapping regions exist or data is already present on the disk, the actual size occupied might be less than this value due to shared or reused map data.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-sizeOnNetworkInBytes" class="section detail">

    ### sizeOnNetworkInBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">sizeOnNetworkInBytes</span>

    </div>

    <div class="block">

    Region size, for downloading/during network operations, in bytes. Regions are downloaded in compressed form and hence they have reduced size on network. Note: This value represents the theoretical maximum size required for the region during transfer. If overlapping data already exists, the actual size downloaded may be smaller due to map data reuse.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-childRegions" class="section detail">

    ### childRegions

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader">Region</a>\></span> <span class="element-name">childRegions</span>

    </div>

    <div class="block">

    All child regions for current region. Note that each child can again contain multiple children. A downloadable region will contain the content of all children.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-navigability" class="section detail">

    ### navigability

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-navigabilitytype" title="enum class in com.here.sdk.maploader">NavigabilityType</a></span> <span class="element-name">navigability</span>

    </div>

    <div class="block">

    Indicates the navigability type of this region.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-maploader-RegionId" class="section detail">

    ### Region

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Region</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> regionId)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `regionId` -

    Unique identifier specifying a region.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


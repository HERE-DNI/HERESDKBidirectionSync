---
title: "CatalogUpdateInfo (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.maploader.CatalogUpdateInfo → com.here.sdk.maploader.CatalogUpdateInfo

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">CatalogUpdateInfo</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Holds information for the catalog update intent. Provides information regarding installed catalog and its latest available version.

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

  `long`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#diskSizeInBytes" class="member-name-link"><code>diskSizeInBytes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Estimates the size of the offline maps after an update.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-installedcatalog" title="class in com.here.sdk.maploader">`InstalledCatalog`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#installedCatalog" class="member-name-link"><code>installedCatalog</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Installed catalog.

  </div>

  </div>

  <div class="col-first even-row-color">

  `long`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#latestVersion" class="member-name-link"><code>latestVersion</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Latest version available for a catalog.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `long`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#networkSizeInBytes" class="member-name-link"><code>networkSizeInBytes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Total size in bytes that needs to be downloaded over the network to update the installed catalog.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatestate" title="enum class in com.here.sdk.maploader">`CatalogUpdateState`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#state" class="member-name-link"><code>state</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  State of current catalog update.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `long`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#temporaryDiskRequirementInBytes" class="member-name-link"><code>temporaryDiskRequirementInBytes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Performing an update requires additional storage on top of existing offline maps.

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

  - <div id="sdk-for-android-navigate-installedCatalog" class="section detail">

    ### installedCatalog

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-installedcatalog" title="class in com.here.sdk.maploader">InstalledCatalog</a></span> <span class="element-name">installedCatalog</span>

    </div>

    <div class="block">

    Installed catalog.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-latestVersion" class="section detail">

    ### latestVersion

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">latestVersion</span>

    </div>

    <div class="block">

    Latest version available for a catalog.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-state" class="section detail">

    ### state

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatestate" title="enum class in com.here.sdk.maploader">CatalogUpdateState</a></span> <span class="element-name">state</span>

    </div>

    <div class="block">

    State of current catalog update.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-networkSizeInBytes" class="section detail">

    ### networkSizeInBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">networkSizeInBytes</span>

    </div>

    <div class="block">

    Total size in bytes that needs to be downloaded over the network to update the installed catalog.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-diskSizeInBytes" class="section detail">

    ### diskSizeInBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">diskSizeInBytes</span>

    </div>

    <div class="block">

    Estimates the size of the offline maps after an update. Note In order to estimate, if catalog update is feasible, given the amount of free space on the disk, application can compare amount of the free space on the disk with disk_size_in_bytes + temporary_disk_requirement_in_bytes .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-temporaryDiskRequirementInBytes" class="section detail">

    ### temporaryDiskRequirementInBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">temporaryDiskRequirementInBytes</span>

    </div>

    <div class="block">

    Performing an update requires additional storage on top of existing offline maps. This space is used to store intermittent copy of map content according to the specified MapUpdater.MapUpdateVersionCommitPolicy . Note In order to estimate, if catalog update is feasible, given the amount of free space on the disk, application can compare amount of the free space on the disk with disk_size_in_bytes + temporary_disk_requirement_in_bytes .

    </div>

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


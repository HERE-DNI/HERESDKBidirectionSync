---
title: "PersistentMapStatus (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< PersistentMapStatus \> com.here.sdk.maploader.PersistentMapStatus → java.lang.Enum \< PersistentMapStatus \> com.here.sdk.maploader.PersistentMapStatus → com.here.sdk.maploader.PersistentMapStatus

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">`PersistentMapStatus`</a>`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">PersistentMapStatus</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>\></span>

</div>

<div class="block">

Specifies possible statuses of the already downloaded map regions as a whole. Note: This can be valid only for a single region in case of a CORRUPTED state.

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>` extends `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang"><code>Enum</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-navigate-enum-constant-summary" class="section constants-summary">

  ## Enum Constant Summary

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#BROKEN_UPDATE" class="member-name-link"><code>BROKEN_UPDATE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Unrecoverable error during construction of pending update parameters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#CORRUPTED" class="member-name-link"><code>CORRUPTED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  One or more downloaded regions failed to open and a repair action should be performed to mitigate this issue.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#INVALID_PATH" class="member-name-link"><code>INVALID_PATH</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Unreachable SDKOptions.cachePath or SDKOptions.persistentMapStoragePath .

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#INVALID_STATE" class="member-name-link"><code>INVALID_STATE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Unrecoverable error during construction of internal map access object.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#MIGRATION_NEEDED" class="member-name-link"><code>MIGRATION_NEEDED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates that the downloaded regions need to be migrated to a new internal format by calling sdk.maploader.MapDownloader.repair_persistent_map .

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#OK" class="member-name-link"><code>OK</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  All downloaded regions are in a workable state, no issues found.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#PENDING_UPDATE" class="member-name-link"><code>PENDING_UPDATE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A map update operation initiated by a user has been interrupted.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#STORAGE_CLOSED" class="member-name-link"><code>STORAGE_CLOSED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of SDKNativeEngine .

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">`PersistentMapStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">`PersistentMapStatus`</a>`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" class="external-link" title="class or interface in java.lang"><code>compareTo</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" class="external-link" title="class or interface in java.lang"><code>describeConstable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" class="external-link" title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" class="external-link" title="class or interface in java.lang"><code>name</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" class="external-link" title="class or interface in java.lang"><code>ordinal</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" class="external-link" title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-enum-constant-detail" class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-navigate-OK" class="section detail">

    ### OK

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">OK</span>

    </div>

    <div class="block">

    All downloaded regions are in a workable state, no issues found.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-CORRUPTED" class="section detail">

    ### CORRUPTED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">CORRUPTED</span>

    </div>

    <div class="block">

    One or more downloaded regions failed to open and a repair action should be performed to mitigate this issue. All map download and map update operations (except for sdk.maploader.MapDownloader.repair_persistent_map ) will return sdk.maploader.MapLoaderError.NOT_READY .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-BROKEN_UPDATE" class="section detail">

    ### BROKEN_UPDATE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">BROKEN_UPDATE</span>

    </div>

    <div class="block">

    Unrecoverable error during construction of pending update parameters. Operations such as catalog updates or region downloads will fail. The healing procedure is to clean persistent map with sdk.maploader.MapDownloader.clear_persistent_map_storage .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-MIGRATION_NEEDED" class="section detail">

    ### MIGRATION_NEEDED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">MIGRATION_NEEDED</span>

    </div>

    <div class="block">

    Indicates that the downloaded regions need to be migrated to a new internal format by calling sdk.maploader.MapDownloader.repair_persistent_map . This error is not a result of a data loss, nor any data will be lost when performing the repair operation and the map version will stay unchanged afterwards.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-PENDING_UPDATE" class="section detail">

    ### PENDING_UPDATE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">PENDING_UPDATE</span>

    </div>

    <div class="block">

    A map update operation initiated by a user has been interrupted. Calls to sdk.maploader.MapDownloader.download_regions and sdk.maploader.MapDownloader.delete_regions will fail with sdk.maploader.MapLoaderError.INTERNAL_ERROR . To repair a map, call again sdk.maploader.MapUpdater.update_catalog for the affected catalog. sdk.maploader.MapUpdater.retrieve_catalogs_update_info returns a list of sdk.maploader.CatalogUpdateInfo items: The affected catalog can be identified by the state, which is set to sdk.maploader.CatalogUpdateState.PENDING_UPDATE . To know if a map needs to be repaired, check if sdk.maploader.MapLoaderError.PENDING_UPDATE has occurred.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-INVALID_PATH" class="section detail">

    ### INVALID_PATH

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">INVALID_PATH</span>

    </div>

    <div class="block">

    Unreachable SDKOptions.cachePath or SDKOptions.persistentMapStoragePath . Make sure that SDKOptions has accessible SDKOptions.cachePath and SDKOptions.persistentMapStoragePath

    </div>

    </div>

  - <div id="sdk-for-android-navigate-INVALID_STATE" class="section detail">

    ### INVALID_STATE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">INVALID_STATE</span>

    </div>

    <div class="block">

    Unrecoverable error during construction of internal map access object. The healing procedure is to clean persistent map with sdk.maploader.MapDownloader.clear_persistent_map_storage .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-STORAGE_CLOSED" class="section detail">

    ### STORAGE_CLOSED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">STORAGE_CLOSED</span>

    </div>

    <div class="block">

    Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of SDKNativeEngine .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order they are declared

    </div>

  - <div id="sdk-for-android-navigate-valueOf-java-lang-String" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The string must match exactly an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if this enum class has no constant with the specified name

    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" class="external-link" title="class or interface in java.lang"><code>NullPointerException</code></a> - if the argument is null

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


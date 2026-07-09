---
title: "MapLoaderError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-maploadererror"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< MapLoaderError \> com.here.sdk.maploader.MapLoaderError → java.lang.Enum \< MapLoaderError \> com.here.sdk.maploader.MapLoaderError → com.here.sdk.maploader.MapLoaderError

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">`MapLoaderError`</a>`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">MapLoaderError</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>\></span>

</div>

<div class="block">

Specifies possible errors that may result from map downloading/prefetching.

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

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#ACCESS_DENIED" class="member-name-link"><code>ACCESS_DENIED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The access is denied due to invalid credentials.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#ALREADY_INSTALLED" class="member-name-link"><code>ALREADY_INSTALLED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  All tiles of requested regions were already installed, no need for any download.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#BROKEN_UPDATE" class="member-name-link"><code>BROKEN_UPDATE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Unrecoverable error during construction of pending update parameters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#CACHE_IO_ERROR" class="member-name-link"><code>CACHE_IO_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A cache IO error occurred.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#CATALOG_CONFIGURATION_ERROR" class="member-name-link"><code>CATALOG_CONFIGURATION_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Misconfiguration of catalogs.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#FORBIDDEN" class="member-name-link"><code>FORBIDDEN</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The operation is forbidden, make sure your credentials grant the necessary permissions.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#INCOMPLETE_DATA" class="member-name-link"><code>INCOMPLETE_DATA</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The data to process is incomplete, failed decoding the tile.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#INTERNAL_ERROR" class="member-name-link"><code>INTERNAL_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Internal error occurred.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#INVALID_ARGUMENT" class="member-name-link"><code>INVALID_ARGUMENT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The request passed invalid arguments.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#MAP_DATA_ERROR" class="member-name-link"><code>MAP_DATA_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Downloaded map data is invalid or a sdk.maploader.RegionId passed to the method sdk.maploader.MapDownloader.delete_regions is incorrect.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#MAP_MANAGER_ERROR" class="member-name-link"><code>MAP_MANAGER_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Error occurred inside the map manager and might be related to network issues.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#MIGRATION_REQUIRED" class="member-name-link"><code>MIGRATION_REQUIRED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Operation on the protected cache cannot be done due to required migration.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#NETWORK_CONNECTION_ERROR" class="member-name-link"><code>NETWORK_CONNECTION_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A network connection error has happened.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#NOT_ENOUGH_SPACE" class="member-name-link"><code>NOT_ENOUGH_SPACE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  There's no sufficient space on the disk to finish operation.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#NOT_READY" class="member-name-link"><code>NOT_READY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  There's a problem with an ongoing download or update: If an operation is in a paused state, you can resume or cancel it.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#OFFLINE" class="member-name-link"><code>OFFLINE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Online operation is not permitted because offline mode is enabled.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#ONLINE_NAVIGATE_ONLY" class="member-name-link"><code>ONLINE_NAVIGATE_ONLY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This version of HERE SDK does not support the ability to download maps.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#OPERATION_AFTER_DISPOSE" class="member-name-link"><code>OPERATION_AFTER_DISPOSE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Method is invoked on object connected to the disposed SDKNativeEngine.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#OPERATION_CANCELLED" class="member-name-link"><code>OPERATION_CANCELLED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The request was cancelled (usually by the user).

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PARALLEL_REQUEST" class="member-name-link"><code>PARALLEL_REQUEST</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PENDING_UPDATE" class="member-name-link"><code>PENDING_UPDATE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map regions update was interrupted.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PROTECTED_CACHE_CORRUPTED" class="member-name-link"><code>PROTECTED_CACHE_CORRUPTED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Protected cache is corrupted.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PROXY_AUTHENTICATION_FAILED" class="member-name-link"><code>PROXY_AUTHENTICATION_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Proxy is not authenticated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PROXY_SERVER_UNREACHABLE" class="member-name-link"><code>PROXY_SERVER_UNREACHABLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Proxy server unreachable.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#REQUEST_LIMIT_REACHED" class="member-name-link"><code>REQUEST_LIMIT_REACHED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Request limit reached for set a credentials for a particular period of time.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#RESOURCE_NOT_FOUND" class="member-name-link"><code>RESOURCE_NOT_FOUND</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The requested resource is not found.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#SERVICE_ACCESS_FAILED" class="member-name-link"><code>SERVICE_ACCESS_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The conditions to access the service are not satisfied.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#SERVICE_UNAVAILABLE" class="member-name-link"><code>SERVICE_UNAVAILABLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The requested service is unavailable.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#TIME_OUT" class="member-name-link"><code>TIME_OUT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The request exceeded the timeout limit.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#UNEXPECTED_SERVER_RESPONSE" class="member-name-link"><code>UNEXPECTED_SERVER_RESPONSE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Received unexpected response from the backend.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#UPDATE_BLOCKED_AS_ANOTHER_PENDING" class="member-name-link"><code>UPDATE_BLOCKED_AS_ANOTHER_PENDING</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state.

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

  `static `<a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">`MapLoaderError`</a>

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

  `static `<a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">`MapLoaderError`</a>`[]`

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

  - <div id="sdk-for-android-navigate-RESOURCE_NOT_FOUND" class="section detail">

    ### RESOURCE_NOT_FOUND

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">RESOURCE_NOT_FOUND</span>

    </div>

    <div class="block">

    The requested resource is not found.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-NOT_READY" class="section detail">

    ### NOT_READY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">NOT_READY</span>

    </div>

    <div class="block">

    There's a problem with an ongoing download or update: If an operation is in a paused state, you can resume or cancel it. If no operation is in a paused state: Either wait for active downloads to finish, or cancel existing sdk.maploader.MapDownloader requests and call sdk.maploader.MapDownloader.get_initial_persistent_map_status . If there is a problem, call sdk.maploader.MapDownloader.repair_persistent_map to repair before continuing with other sdk.maploader.MapDownloader operations. This error may occur when an on-going or paused operation prevents the requested task.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-INVALID_ARGUMENT" class="section detail">

    ### INVALID_ARGUMENT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">INVALID_ARGUMENT</span>

    </div>

    <div class="block">

    The request passed invalid arguments.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-OPERATION_CANCELLED" class="section detail">

    ### OPERATION_CANCELLED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">OPERATION_CANCELLED</span>

    </div>

    <div class="block">

    The request was cancelled (usually by the user).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-ALREADY_INSTALLED" class="section detail">

    ### ALREADY_INSTALLED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">ALREADY_INSTALLED</span>

    </div>

    <div class="block">

    All tiles of requested regions were already installed, no need for any download.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-TIME_OUT" class="section detail">

    ### TIME_OUT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">TIME_OUT</span>

    </div>

    <div class="block">

    The request exceeded the timeout limit.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-SERVICE_UNAVAILABLE" class="section detail">

    ### SERVICE_UNAVAILABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">SERVICE_UNAVAILABLE</span>

    </div>

    <div class="block">

    The requested service is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-ACCESS_DENIED" class="section detail">

    ### ACCESS_DENIED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">ACCESS_DENIED</span>

    </div>

    <div class="block">

    The access is denied due to invalid credentials.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-REQUEST_LIMIT_REACHED" class="section detail">

    ### REQUEST_LIMIT_REACHED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">REQUEST_LIMIT_REACHED</span>

    </div>

    <div class="block">

    Request limit reached for set a credentials for a particular period of time.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-NETWORK_CONNECTION_ERROR" class="section detail">

    ### NETWORK_CONNECTION_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">NETWORK_CONNECTION_ERROR</span>

    </div>

    <div class="block">

    A network connection error has happened.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-FORBIDDEN" class="section detail">

    ### FORBIDDEN

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">FORBIDDEN</span>

    </div>

    <div class="block">

    The operation is forbidden, make sure your credentials grant the necessary permissions.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-MAP_DATA_ERROR" class="section detail">

    ### MAP_DATA_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">MAP_DATA_ERROR</span>

    </div>

    <div class="block">

    Downloaded map data is invalid or a sdk.maploader.RegionId passed to the method sdk.maploader.MapDownloader.delete_regions is incorrect.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-UNEXPECTED_SERVER_RESPONSE" class="section detail">

    ### UNEXPECTED_SERVER_RESPONSE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">UNEXPECTED_SERVER_RESPONSE</span>

    </div>

    <div class="block">

    Received unexpected response from the backend. It means the response is malformed or server returned an internal error. Try repeating the request.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-MAP_MANAGER_ERROR" class="section detail">

    ### MAP_MANAGER_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">MAP_MANAGER_ERROR</span>

    </div>

    <div class="block">

    Error occurred inside the map manager and might be related to network issues. Try repeating the request.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-INCOMPLETE_DATA" class="section detail">

    ### INCOMPLETE_DATA

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">INCOMPLETE_DATA</span>

    </div>

    <div class="block">

    The data to process is incomplete, failed decoding the tile.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-SERVICE_ACCESS_FAILED" class="section detail">

    ### SERVICE_ACCESS_FAILED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">SERVICE_ACCESS_FAILED</span>

    </div>

    <div class="block">

    The conditions to access the service are not satisfied. Check if correct sdk.maploader.RegionId was passed to sdk.maploader.MapDownloader.download_regions or download for passed sdk.maploader.RegionId already started. Further control for started download must be performed through sdk.maploader.MapDownloaderTask .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-INTERNAL_ERROR" class="section detail">

    ### INTERNAL_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">INTERNAL_ERROR</span>

    </div>

    <div class="block">

    Internal error occurred.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-OFFLINE" class="section detail">

    ### OFFLINE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">OFFLINE</span>

    </div>

    <div class="block">

    Online operation is not permitted because offline mode is enabled.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-CACHE_IO_ERROR" class="section detail">

    ### CACHE_IO_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">CACHE_IO_ERROR</span>

    </div>

    <div class="block">

    A cache IO error occurred.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-PROTECTED_CACHE_CORRUPTED" class="section detail">

    ### PROTECTED_CACHE_CORRUPTED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PROTECTED_CACHE_CORRUPTED</span>

    </div>

    <div class="block">

    Protected cache is corrupted. It can be a result of downloading the map in the background and the OS killing the application at that time. Use method sdk.maploader.MapDownloader.get_initial_persistent_map_status to get the status of the map and method repair_persistent_map in the MapDownloader to try to fix the cache if it is broken.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-MIGRATION_REQUIRED" class="section detail">

    ### MIGRATION_REQUIRED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">MIGRATION_REQUIRED</span>

    </div>

    <div class="block">

    Operation on the protected cache cannot be done due to required migration. Call sdk.maploader.MapDownloader.repair_persistent_map to perform migration.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-OPERATION_AFTER_DISPOSE" class="section detail">

    ### OPERATION_AFTER_DISPOSE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">OPERATION_AFTER_DISPOSE</span>

    </div>

    <div class="block">

    Method is invoked on object connected to the disposed SDKNativeEngine.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-CATALOG_CONFIGURATION_ERROR" class="section detail">

    ### CATALOG_CONFIGURATION_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">CATALOG_CONFIGURATION_ERROR</span>

    </div>

    <div class="block">

    Misconfiguration of catalogs. This error may occur when sdk.core.engine.CatalogConfiguration is misconfigured and cannot be used for any operation with MapDownloader or MapUpdater . Verify SDKOptions.catalogConfigurations .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-PENDING_UPDATE" class="section detail">

    ### PENDING_UPDATE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PENDING_UPDATE</span>

    </div>

    <div class="block">

    Map regions update was interrupted. Indicates that the cache state is wrong after an update that was finished not in correct way (e.g sudden app shutdown). Prefetching or removing of map regions are blocked until the update has been completed successfully.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-UPDATE_BLOCKED_AS_ANOTHER_PENDING" class="section detail">

    ### UPDATE_BLOCKED_AS_ANOTHER_PENDING

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">UPDATE_BLOCKED_AS_ANOTHER_PENDING</span>

    </div>

    <div class="block">

    Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state. Update the catalog in PENDING_UPDATE state first, before trying to update another catalog.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-BROKEN_UPDATE" class="section detail">

    ### BROKEN_UPDATE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">BROKEN_UPDATE</span>

    </div>

    <div class="block">

    Unrecoverable error during construction of pending update parameters. Operations such as catalog updates or region downloads will fail. The healing procedure is to clean persistent map with sdk.maploader.MapDownloader.clear_persistent_map_storage .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-PARALLEL_REQUEST" class="section detail">

    ### PARALLEL_REQUEST

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PARALLEL_REQUEST</span>

    </div>

    <div class="block">

    Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)

    </div>

    </div>

  - <div id="sdk-for-android-navigate-PROXY_AUTHENTICATION_FAILED" class="section detail">

    ### PROXY_AUTHENTICATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PROXY_AUTHENTICATION_FAILED</span>

    </div>

    <div class="block">

    Proxy is not authenticated. Check your proxy credentials.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-PROXY_SERVER_UNREACHABLE" class="section detail">

    ### PROXY_SERVER_UNREACHABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PROXY_SERVER_UNREACHABLE</span>

    </div>

    <div class="block">

    Proxy server unreachable.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-NOT_ENOUGH_SPACE" class="section detail">

    ### NOT_ENOUGH_SPACE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">NOT_ENOUGH_SPACE</span>

    </div>

    <div class="block">

    There's no sufficient space on the disk to finish operation. For offline maps operation (download or update), it means that there's not enough space on the device. For prefetch operations, it means that there's not enough space in the mutable cache to store the prefetched data.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-ONLINE_NAVIGATE_ONLY" class="section detail">

    ### ONLINE_NAVIGATE_ONLY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">ONLINE_NAVIGATE_ONLY</span>

    </div>

    <div class="block">

    This version of HERE SDK does not support the ability to download maps. Contact the sales team to get access to the full version.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>\[\]</span> <span class="element-name">values</span>()

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

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

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


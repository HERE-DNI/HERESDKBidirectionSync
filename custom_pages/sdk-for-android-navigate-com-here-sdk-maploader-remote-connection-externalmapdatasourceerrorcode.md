---
title: "ExternalMapDataSourceErrorCode (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-package-summary">com.here.sdk.maploader.remote.connection</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< ExternalMapDataSourceErrorCode \> com.here.sdk.maploader.remote.connection.ExternalMapDataSourceErrorCode → java.lang.Enum \< ExternalMapDataSourceErrorCode \> com.here.sdk.maploader.remote.connection.ExternalMapDataSourceErrorCode → com.here.sdk.maploader.remote.connection.ExternalMapDataSourceErrorCode

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">`ExternalMapDataSourceErrorCode`</a>`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">ExternalMapDataSourceErrorCode</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a>\></span>

</div>

<div class="block">

Describes the reason for failing to configure SDKNativeEngine with external map data source. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode#ADD_CATALOG_ERROR" class="member-name-link"><code>ADD_CATALOG_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Error while adding catalog to DataStoreClient .

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode#CLIENT_DISPOSED_ERROR" class="member-name-link"><code>CLIENT_DISPOSED_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  While attempting to register the connection, the client was being disposed

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode#INTERNAL_ERROR" class="member-name-link"><code>INTERNAL_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Internal error occurred.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode#INVALID_CREDENTIALS" class="member-name-link"><code>INVALID_CREDENTIALS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Error while checking credentials.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode#SERVER_UNAVAILABLE" class="member-name-link"><code>SERVER_UNAVAILABLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This means that server is not launched or configuration settings is wrong.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode#SERVICE_REGISTER_ERROR" class="member-name-link"><code>SERVICE_REGISTER_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Error while attempting to register OCM AM service

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

  `static `<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">`ExternalMapDataSourceErrorCode`</a>

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

  `static `<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">`ExternalMapDataSourceErrorCode`</a>`[]`

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

  - <div id="sdk-for-android-navigate-INTERNAL_ERROR" class="section detail">

    ### INTERNAL_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></span> <span class="element-name">INTERNAL_ERROR</span>

    </div>

    <div class="block">

    Internal error occurred.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-ADD_CATALOG_ERROR" class="section detail">

    ### ADD_CATALOG_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></span> <span class="element-name">ADD_CATALOG_ERROR</span>

    </div>

    <div class="block">

    Error while adding catalog to DataStoreClient . Verify the same catalogs are added to the DataStoreServer instance on the server side.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-INVALID_CREDENTIALS" class="section detail">

    ### INVALID_CREDENTIALS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></span> <span class="element-name">INVALID_CREDENTIALS</span>

    </div>

    <div class="block">

    Error while checking credentials. E.g. some field is empty but expected not empty

    </div>

    </div>

  - <div id="sdk-for-android-navigate-SERVICE_REGISTER_ERROR" class="section detail">

    ### SERVICE_REGISTER_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></span> <span class="element-name">SERVICE_REGISTER_ERROR</span>

    </div>

    <div class="block">

    Error while attempting to register OCM AM service

    </div>

    </div>

  - <div id="sdk-for-android-navigate-CLIENT_DISPOSED_ERROR" class="section detail">

    ### CLIENT_DISPOSED_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></span> <span class="element-name">CLIENT_DISPOSED_ERROR</span>

    </div>

    <div class="block">

    While attempting to register the connection, the client was being disposed

    </div>

    </div>

  - <div id="sdk-for-android-navigate-SERVER_UNAVAILABLE" class="section detail">

    ### SERVER_UNAVAILABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></span> <span class="element-name">SERVER_UNAVAILABLE</span>

    </div>

    <div class="block">

    This means that server is not launched or configuration settings is wrong. Make sense only on client side

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a>\[\]</span> <span class="element-name">values</span>()

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

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

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


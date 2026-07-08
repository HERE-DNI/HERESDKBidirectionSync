---
title: "ProxySettings (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-proxysettings"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.core.engine.ProxySettings → com.here.sdk.core.engine.ProxySettings

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ProxySettings</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Proxy configuration for the HERE SDK network that is applied per request. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-credentials" class="type-name-link" title="class in com.here.sdk.core.engine"><code>ProxySettings.Credentials</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Authentication data

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static enum `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype" class="type-name-link" title="enum class in com.here.sdk.core.engine"><code>ProxySettings.ProxyType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Supported types of proxy connection.

  </div>

  </div>

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

  [`ProxySettings.Credentials`](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-credentials "class in com.here.sdk.core.engine")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#credentials" class="member-name-link"><code>credentials</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional field to define credentials to authenticate a user to the proxy server.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html" class="external-link" title="class or interface in java.net"><code>InetAddress</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#ipAddress" class="member-name-link"><code>ipAddress</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Represents the IP Address of the proxy server.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#networkInterface" class="member-name-link"><code>networkInterface</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Network interface.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#port" class="member-name-link"><code>port</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Represents the port number of the proxy server.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`ProxySettings.ProxyType`](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#type" class="member-name-link"><code>type</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Represents the type of the proxy server.

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

      ProxySettings ( ProxySettings.ProxyType type, InetAddress ipAddress,
       int port)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[ProxySettings.ProxyType](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype "enum class in com.here.sdk.core.engine")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Represents the type of the proxy server.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ipAddress" class="section detail">

    ### ipAddress

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html" class="external-link" title="class or interface in java.net">InetAddress</a></span> <span class="element-name">ipAddress</span>

    </div>

    <div class="block">

    Represents the IP Address of the proxy server.

    </div>

    </div>

  - <div id="sdk-for-android-explore-networkInterface" class="section detail">

    ### networkInterface

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">networkInterface</span>

    </div>

    <div class="block">

    Network interface. It's taken into account when IPv6 is used. Default value is "wlan0". If not set then no interface is used.

    </div>

    </div>

  - <div id="sdk-for-android-explore-port" class="section detail">

    ### port

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">port</span>

    </div>

    <div class="block">

    Represents the port number of the proxy server.

    </div>

    </div>

  - <div id="sdk-for-android-explore-credentials" class="section detail">

    ### credentials

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[ProxySettings.Credentials](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-credentials "class in com.here.sdk.core.engine")</span> <span class="element-name">credentials</span>

    </div>

    <div class="block">

    Optional field to define credentials to authenticate a user to the proxy server.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-engine-ProxySettings-ProxyType-java-net-InetAddress-int" class="section detail">

    ### ProxySettings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ProxySettings</span><wbr></wbr><span class="parameters">(@NonNull [ProxySettings.ProxyType](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype "enum class in com.here.sdk.core.engine") type, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html" class="external-link" title="class or interface in java.net">InetAddress</a> ipAddress, int port)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `type` -

    Represents the type of the proxy server.

    `ipAddress` -

    Represents the IP Address of the proxy server.

    `port` -

    Represents the port number of the proxy server.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


---
title: "ProxySettings (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-proxysettings"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.engine.ProxySettings

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">ProxySettings</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Proxy configuration for the HERE SDK network that is applied per
request. Note: This is a beta release of this feature, so there could be
a few bugs and unexpected behaviors. Related APIs may change for new
releases without a deprecation process.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

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
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-credentials"
  class="type-name-link"
  title="class in com.here.sdk.core.engine"><code>ProxySettings.Credentials</code></a></td>
  <td><div class="block">
  Authentication data
  </div></td>
  </tr>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype"
  class="type-name-link"
  title="enum class in com.here.sdk.core.engine"><code>ProxySettings.ProxyType</code></a></td>
  <td><div class="block">
  Supported types of proxy connection.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-credentials"
  title="class in com.here.sdk.core.engine"><code>ProxySettings.Credentials</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#credentials"
  class="member-name-link"><code>credentials</code></a></td>
  <td><div class="block">
  Optional field to define credentials to authenticate a user to the proxy
  server.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html"
  class="external-link"
  title="class or interface in java.net"><code>InetAddress</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#ipAddress"
  class="member-name-link"><code>ipAddress</code></a></td>
  <td><div class="block">
  Represents the IP Address of the proxy server.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#networkInterface"
  class="member-name-link"><code>networkInterface</code></a></td>
  <td><div class="block">
  Network interface.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#port"
  class="member-name-link"><code>port</code></a></td>
  <td><div class="block">
  Represents the port number of the proxy server.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype"
  title="enum class in com.here.sdk.core.engine"><code>ProxySettings.ProxyType</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings#type"
  class="member-name-link"><code>type</code></a></td>
  <td><div class="block">
  Represents the type of the proxy server.
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
  <td><pre><code>ProxySettings(ProxySettings.ProxyType type,
   InetAddress ipAddress,
   int port)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
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

  - <div id="type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[ProxySettings.ProxyType](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype "enum class in com.here.sdk.core.engine")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Represents the type of the proxy server.

    </div>

    </div>

  - <div id="ipAddress" class="section detail">

    ### ipAddress

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html"
    class="external-link"
    title="class or interface in java.net">InetAddress</a></span> <span class="element-name">ipAddress</span>

    </div>

    <div class="block">

    Represents the IP Address of the proxy server.

    </div>

    </div>

  - <div id="networkInterface" class="section detail">

    ### networkInterface

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">networkInterface</span>

    </div>

    <div class="block">

    Network interface. It's taken into account when IPv6 is used.
    Default value is "wlan0". If not set then no interface is used.

    </div>

    </div>

  - <div id="port" class="section detail">

    ### port

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">port</span>

    </div>

    <div class="block">

    Represents the port number of the proxy server.

    </div>

    </div>

  - <div id="credentials" class="section detail">

    ### credentials

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ProxySettings.Credentials](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-credentials "class in com.here.sdk.core.engine")</span> <span class="element-name">credentials</span>

    </div>

    <div class="block">

    Optional field to define credentials to authenticate a user to the
    proxy server.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.engine.ProxySettings.ProxyType,java.net.InetAddress,int)"
    class="section detail">

    ### ProxySettings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ProxySettings</span><span class="parameters">(@NonNull
    [ProxySettings.ProxyType](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype "enum class in com.here.sdk.core.engine") type,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html"
    class="external-link"
    title="class or interface in java.net">InetAddress</a> ipAddress,
    int port)</span>

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

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>


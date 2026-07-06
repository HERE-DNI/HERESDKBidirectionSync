---
title: "UsageStats.NetworkStats (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.engine.UsageStats.NetworkStats

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[UsageStats](sdk-for-android-explore-com-here-sdk-core-engine-usagestats "class in com.here.sdk.core.engine")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">UsageStats.NetworkStats</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Provides network statistics in bytes per method.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats#methodCall"
  class="member-name-link"><code>methodCall</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Name or description of the method being called.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `long`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats#receivedBytes"
  class="member-name-link"><code>receivedBytes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Number of bytes received from the network.

  </div>

  </div>

  <div class="col-first even-row-color">

  `long`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats#requestCounter"
  class="member-name-link"><code>requestCounter</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Amount of calls for particular family of methodCall.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `long`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats#sentBytes"
  class="member-name-link"><code>sentBytes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Number of bytes sent over the network.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-constructor-summary"
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

      NetworkStats(long sentBytes,
       long receivedBytes,
       String methodCall,
       long requestCounter)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
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
<div id="sdk-for-android-explore-field-detail"
  class="section field-details">
<div id="sdk-for-android-explore-sentBytes" class="section detail">

    ### sentBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">sentBytes</span>

    </div>

    <div class="block">

    Number of bytes sent over the network.

    </div>

    </div>
<div id="sdk-for-android-explore-receivedBytes"
    class="section detail">

    ### receivedBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">receivedBytes</span>

    </div>

    <div class="block">

    Number of bytes received from the network.

    </div>

    </div>
<div id="sdk-for-android-explore-methodCall" class="section detail">

    ### methodCall

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">methodCall</span>

    </div>

    <div class="block">

    Name or description of the method being called.

    </div>

    </div>
<div id="sdk-for-android-explore-requestCounter"
    class="section detail">

    ### requestCounter

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">requestCounter</span>

    </div>

    <div class="block">

    Amount of calls for particular family of methodCall. methodCall in
    this case is considered as base request, additional query params are
    ignored, all calculated as one request. e.g.
    https://search.hereapi.com/someparams and
    https://search.hereapi.com/someparams2 will be considered as 1
    methodCall, and requestCounter is 2.

    </div>

    </div>

  </div>
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>(long,long,java.lang.String,long)"
    class="section detail">

    ### NetworkStats

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">NetworkStats</span><span class="parameters">(long sentBytes,
    long receivedBytes, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> methodCall,
    long requestCounter)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `sentBytes` -

    Number of bytes sent over the network.

    `receivedBytes` -

    Number of bytes received from the network.

    `methodCall` -

    Name or description of the method being called.

    `requestCounter` -

    Amount of calls for particular family of methodCall. methodCall in
    this case is considered as base request, additional query params are
    ignored, all calculated as one request. e.g.
    https://search.hereapi.com/someparams and
    https://search.hereapi.com/someparams2 will be considered as 1
    methodCall, and requestCounter is 2.

    </div>

  </div>

</div>


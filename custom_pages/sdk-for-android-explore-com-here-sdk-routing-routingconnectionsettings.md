---
title: "RoutingConnectionSettings (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.RoutingConnectionSettings →
com.here.sdk.routing.RoutingConnectionSettings

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RoutingConnectionSettings</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Defines the settings for the retry logic when connecting to the HERE
routing backend. When a timeout is triggered, the next connection
attempt starts with a increased timeout. new_timeout = initial_timeout +
increment \* retry_count

</div>

</div>

- <div id="sdk-for-android-explore-field-summary"
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

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings#connectionTimeoutRetryIncrease"
  class="member-name-link"><code>connectionTimeoutRetryIncrease</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines the increase of the timeout for the transfer of data.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings#initialConnectionTimeout"
  class="member-name-link"><code>initialConnectionTimeout</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the initial time out for connection to the backend.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings#initialTransferTimeout"
  class="member-name-link"><code>initialTransferTimeout</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines the initial time out for data transfer from the backend.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings#maxRetryCount"
  class="member-name-link"><code>maxRetryCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the max amount of retries before the route request failes with
  connection related error codes.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings#transferTimeoutRetryIncrease"
  class="member-name-link"><code>transferTimeoutRetryIncrease</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines the increase of the timeout for the connection.

  </div>

  </div>

  </div>

  </div>

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

      RoutingConnectionSettings ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-initialConnectionTimeout"
    class="section detail">

    ### initialConnectionTimeout

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">initialConnectionTimeout</span>

    </div>

    <div class="block">

    Defines the initial time out for connection to the backend. By
    default, the initial connection timeout is 5 seconds.

    </div>

    </div>

  - <div id="sdk-for-android-explore-connectionTimeoutRetryIncrease"
    class="section detail">

    ### connectionTimeoutRetryIncrease

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">connectionTimeoutRetryIncrease</span>

    </div>

    <div class="block">

    Defines the increase of the timeout for the transfer of data. By
    default, the initial connection increment per timeout 10 seconds.

    </div>

    </div>

  - <div id="sdk-for-android-explore-initialTransferTimeout"
    class="section detail">

    ### initialTransferTimeout

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">initialTransferTimeout</span>

    </div>

    <div class="block">

    Defines the initial time out for data transfer from the backend. By
    default, the initial transfer timeout is 10 seconds.

    </div>

    </div>

  - <div id="sdk-for-android-explore-transferTimeoutRetryIncrease"
    class="section detail">

    ### transferTimeoutRetryIncrease

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">transferTimeoutRetryIncrease</span>

    </div>

    <div class="block">

    Defines the increase of the timeout for the connection. By default,
    the initial transfer increment per timeout is 2 seconds.

    </div>

    </div>

  - <div id="sdk-for-android-explore-maxRetryCount"
    class="section detail">

    ### maxRetryCount

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">maxRetryCount</span>

    </div>

    <div class="block">

    Defines the max amount of retries before the route request failes
    with connection related error codes. By default, the max amount of
    retries is 3.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### RoutingConnectionSettings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoutingConnectionSettings</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object"
    class="section detail">

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

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

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


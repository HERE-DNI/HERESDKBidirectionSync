---
title: "AuthenticationMode.AccessTokenProvider (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode-accesstokenprovider"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[AuthenticationMode](sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode "class in com.here.sdk.core.engine")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface
</span><span class="element-name type-name-label">AuthenticationMode.AccessTokenProvider</span>

</div>

<div class="block">

This lambda is used to retrieve access token in synchronous manner. It
returns the access token or null if it is not set. The lambda is called
each time the access token is needed and it is executed on the main
thread of the application.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>apply()</code></pre></td>
  <td><div class="block">
  This lambda is used to retrieve access token in synchronous manner.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="apply()" class="section detail">

    ### apply

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">apply</span>()

    </div>

    <div class="block">

    This lambda is used to retrieve access token in synchronous manner.
    It returns the access token or null if it is not set. The lambda is
    called each time the access token is needed and it is executed on
    the main thread of the application.

    </div>

    Returns:  
    Access token in case it is set or null otherwise.

    </div>

  </div>

</div>


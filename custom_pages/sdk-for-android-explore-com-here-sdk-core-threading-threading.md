---
title: "Threading (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-threading-threading"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.threading](sdk-for-android-explore-com-here-sdk-core-threading-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.core.threading.Threading →
com.here.NativeBase → com.here.sdk.core.threading.Threading

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Threading</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Initializes threading support on native side.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
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
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-threading-platformthreading"
  title="interface in com.here.sdk.core.threading"><code>PlatformThreading</code></a></td>
  <td><pre><code>getPlatformThreading()</code></pre></td>
  <td><div class="block">
  Returns threading bridge which was set before.
  </div></td>
  </tr>
  <tr>
  <td><code>static void</code></td>
  <td><pre><code>setPlatformThreading(PlatformThreading platformThreading)</code></pre></td>
  <td><div class="block">
  Sets threading bridge which is used for interaction with the platform
  side.
  </div></td>
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

- <div id="method-detail" class="section method-details">

  - <div id="setPlatformThreading(com.here.sdk.core.threading.PlatformThreading)"
    class="section detail">

    ### setPlatformThreading

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setPlatformThreading</span><span class="parameters">(@NonNull
    [PlatformThreading](sdk-for-android-explore-com-here-sdk-core-threading-platformthreading "interface in com.here.sdk.core.threading") platformThreading)</span>

    </div>

    <div class="block">

    Sets threading bridge which is used for interaction with the
    platform side.

    </div>

    Parameters:  
    `platformThreading` -

    Platform threading bridge which should be implemented on the
    platform side.

    </div>

  - <div id="getPlatformThreading()" class="section detail">

    ### getPlatformThreading

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[PlatformThreading](sdk-for-android-explore-com-here-sdk-core-threading-platformthreading "interface in com.here.sdk.core.threading")</span> <span class="element-name">getPlatformThreading</span>()

    </div>

    <div class="block">

    Returns threading bridge which was set before.

    </div>

    Returns:  
    Current platform threading bridge.

    </div>

  </div>

</div>


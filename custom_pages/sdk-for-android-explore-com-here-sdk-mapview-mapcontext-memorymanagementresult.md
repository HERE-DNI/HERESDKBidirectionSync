---
title: "MapContext.MemoryManagementResult (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresult"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.mapview.MapContext.MemoryManagementResult

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapContext.MemoryManagementResult</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Memory management result. Note: This is a beta release of this feature,
so there could be a few bugs and unexpected behavior. Related APIs may
change for new releases without a deprecation process.

</div>

</div>

<div class="section summary">

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresult#diffBetweenVideoMemoryLimitAndRequirementInKiB"
  class="member-name-link"><code>diffBetweenVideoMemoryLimitAndRequirementInKiB</code></a></td>
  <td><div class="block">
  The difference in kibibytes between the limit and the video-memory
  requirement for only the currently visible data.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode"
  title="enum class in com.here.sdk.mapview"><code>MapContext.MemoryManagementResultCode</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresult#resultCode"
  class="member-name-link"><code>resultCode</code></a></td>
  <td><div class="block">
  The result code of the memory management request.
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
  <td><pre><code>MemoryManagementResult(MapContext.MemoryManagementResultCode resultCode)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

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

- <div id="field-detail" class="section field-details">

  - <div id="diffBetweenVideoMemoryLimitAndRequirementInKiB"
    class="section detail">

    ### diffBetweenVideoMemoryLimitAndRequirementInKiB

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">diffBetweenVideoMemoryLimitAndRequirementInKiB</span>

    </div>

    <div class="block">

    The difference in kibibytes between the limit and the video-memory
    requirement for only the currently visible data. If positive, the
    returned value is the surplus value over the currently required bare
    minimum. Even when positive, if the limit set is low, the
    application could later breach the limit and delete even visible
    data. A non positive value means the limit cannot fit the existing
    visible data and there could be data disappearing or flickering. If
    for some reason the callback is ignored or correct memory limit
    cannot be calculated, null value is returned.

    </div>

    </div>

  - <div id="resultCode" class="section detail">

    ### resultCode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">resultCode</span>

    </div>

    <div class="block">

    The result code of the memory management request.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.mapview.MapContext.MemoryManagementResultCode)"
    class="section detail">

    ### MemoryManagementResult

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MemoryManagementResult</span><span class="parameters">(@NonNull
    [MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview") resultCode)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `resultCode` -

    The result code of the memory management request.

    </div>

  </div>

</div>


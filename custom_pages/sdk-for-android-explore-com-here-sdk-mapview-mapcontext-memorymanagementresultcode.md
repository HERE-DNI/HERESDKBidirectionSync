---
title: "MapContext.MemoryManagementResultCode (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
java.lang.Enum<MapContext.MemoryManagementResultCode>com.here.sdk.mapview.MapContext.MemoryManagementResultCode
→ java.lang.Enum → MapContext.MemoryManagementResultCode →
com.here.sdk.mapview.MapContext.MemoryManagementResultCode

</div>

<div id="class-description" class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`MapContext.MemoryManagementResultCode`](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<!-- -->

Enclosing class:  
[MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static enum
</span><span class="element-name type-name-label">MapContext.MemoryManagementResultCode</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a><[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")></span>

</div>

<div class="block">

The memory management result code. Note: This is a beta release of this
feature, so there could be a few bugs and unexpected behavior. Related
APIs may change for new releases without a deprecation process.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>` extends `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="enum-constant-summary" class="section constants-summary">

  <div class="caption">

  Enum Constants

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Enum Constant</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode#APPLIED"
  class="member-name-link"><code>APPLIED</code></a></td>
  <td><div class="block">
  The memory management options were successfully applied.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode#FAILED"
  class="member-name-link"><code>FAILED</code></a></td>
  <td><div class="block">
  The memory management options could not be applied due to other errors.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode#FAILED_BOTH_MEMORY_LIMITS_EXCEEDED"
  class="member-name-link"><code>FAILED_BOTH_MEMORY_LIMITS_EXCEEDED</code></a></td>
  <td><div class="block">
  Both video memory and CPU tile cache limits were exceeded and limits
  were not applied.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode#TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED"
  class="member-name-link"><code>TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED</code></a></td>
  <td><div class="block">
  The requested memory limit exceeds the maximum allowed limit for CPU
  tile cache.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode#VIDEO_MEMORY_LIMIT_EXCEEDED"
  class="member-name-link"><code>VIDEO_MEMORY_LIMIT_EXCEEDED</code></a></td>
  <td><div class="block">
  The requested memory limit exceeds the maximum allowed limit for video
  memory.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode"
  title="enum class in com.here.sdk.mapview"><code>MapContext.MemoryManagementResultCode</code></a></td>
  <td><pre><code>valueOf(String name)</code></pre></td>
  <td><div class="block">
  Returns the enum constant of this class with the specified name.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode"
  title="enum class in com.here.sdk.mapview"><code>MapContext.MemoryManagementResultCode</code></a><code>[]</code></td>
  <td><pre><code>values()</code></pre></td>
  <td><div class="block">
  Returns an array containing the constants of this enum class, in the
  order they are declared.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)"
  class="external-link"
  title="class or interface in java.lang"><code>compareTo</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()"
  class="external-link"
  title="class or interface in java.lang"><code>describeConstable</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getDeclaringClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()"
  class="external-link"
  title="class or interface in java.lang"><code>name</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()"
  class="external-link"
  title="class or interface in java.lang"><code>ordinal</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)"
  class="external-link"
  title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
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

- <div id="enum-constant-detail" class="section constant-details">

  - <div id="APPLIED" class="section detail">

    ### APPLIED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">APPLIED</span>

    </div>

    <div class="block">

    The memory management options were successfully applied.

    </div>

    </div>

  - <div id="TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED"
    class="section detail">

    ### TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">TILE_CACHE_CPU_MEMORY_LIMIT_EXCEEDED</span>

    </div>

    <div class="block">

    The requested memory limit exceeds the maximum allowed limit for CPU
    tile cache. Previous value of CPU tile cache limit is preserved.
    Video memory limit applied correctly.

    </div>

    </div>

  - <div id="VIDEO_MEMORY_LIMIT_EXCEEDED" class="section detail">

    ### VIDEO_MEMORY_LIMIT_EXCEEDED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">VIDEO_MEMORY_LIMIT_EXCEEDED</span>

    </div>

    <div class="block">

    The requested memory limit exceeds the maximum allowed limit for
    video memory. Previous value of video memory limit is preserved. CPU
    tile cache limit applied correctly.

    </div>

    </div>

  - <div id="FAILED_BOTH_MEMORY_LIMITS_EXCEEDED" class="section detail">

    ### FAILED_BOTH_MEMORY_LIMITS_EXCEEDED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">FAILED_BOTH_MEMORY_LIMITS_EXCEEDED</span>

    </div>

    <div class="block">

    Both video memory and CPU tile cache limits were exceeded and limits
    were not applied. Previous values of video memory and CPU tile cache
    limits are preserved.

    </div>

    </div>

  - <div id="FAILED" class="section detail">

    ### FAILED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">FAILED</span>

    </div>

    <div class="block">

    The memory management options could not be applied due to other
    errors.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="values()" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="valueOf(java.lang.String)" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[MapContext.MemoryManagementResultCode](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The
    string must match exactly an identifier used to declare an enum
    constant in this class. (Extraneous whitespace characters are not
    permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if this enum class has no constant with the specified name

    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if the argument is null

    </div>

  </div>

</div>


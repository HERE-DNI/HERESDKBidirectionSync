---
title: "MapContext.MemoryManagementOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.mapview.MapContext.MemoryManagementOptions

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapContext.MemoryManagementOptions</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Memory management options. Note: This is a beta release of this feature,
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
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementstrategy"
  title="enum class in com.here.sdk.mapview"><code>MapContext.MemoryManagementStrategy</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions#memoryManagementStrategy"
  class="member-name-link"><code>memoryManagementStrategy</code></a></td>
  <td><div class="block">
  The default setting MemoryManagementStrategy.DYNAMIC is suitable for
  common cases.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions#tileCacheMemoryLimitInKiB"
  class="member-name-link"><code>tileCacheMemoryLimitInKiB</code></a></td>
  <td><div class="block">
  Tile cache memory limit in kibibytes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions#videoMemoryLimitInKiB"
  class="member-name-link"><code>videoMemoryLimitInKiB</code></a></td>
  <td><div class="block">
  Target video memory limit in kibibytes.
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
  <td><pre><code>MemoryManagementOptions()</code></pre></td>
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

  - <div id="memoryManagementStrategy" class="section detail">

    ### memoryManagementStrategy

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapContext.MemoryManagementStrategy](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementstrategy "enum class in com.here.sdk.mapview")</span> <span class="element-name">memoryManagementStrategy</span>

    </div>

    <div class="block">

    The default setting MemoryManagementStrategy.DYNAMIC is suitable for
    common cases. The map data cache can adjust dynamically to fit
    visible data. When the visible data needs extra memory, it would
    increase. When it's not needed, it will reduce to a limit which is
    calculated internally or by using tileCacheMemoryLimitInKiB option.
    The MemoryManagementStrategy.FIXED would be only useful when there
    is very strict memory consumption requirement for the application.
    It potentially can have flickering visual artifacts when the map
    data to be visualized is very large and exceeds the cache limit.

    </div>

    </div>

  - <div id="tileCacheMemoryLimitInKiB" class="section detail">

    ### tileCacheMemoryLimitInKiB

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">tileCacheMemoryLimitInKiB</span>

    </div>

    <div class="block">

    Tile cache memory limit in kibibytes. Non positive or null values
    are ignored. Default value is null . Low tile cache limit will lead
    to eviction of tiles only if MemoryManagementStrategy is set to
    FIXED.

    </div>

    </div>

  - <div id="videoMemoryLimitInKiB" class="section detail">

    ### videoMemoryLimitInKiB

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">videoMemoryLimitInKiB</span>

    </div>

    <div class="block">

    Target video memory limit in kibibytes. Non positive or null values
    are ignored. Default value is null .

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### MemoryManagementOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MemoryManagementOptions</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

</div>


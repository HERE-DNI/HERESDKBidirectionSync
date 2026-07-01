---
title: "HereMap (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-heremap"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.HereMap →
com.here.NativeBase → com.here.sdk.mapview.HereMap

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">HereMap</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

The representation of a dynamic and interactive geographic map. The map
manages a collection of layers of objects and spaces, presents them in a
stacked layout and offers the means to focus on a certain area. The
layers, their relation to the objects and spaces, the layout and the
representation style is described through a configuration.

</div>

</div>

<div class="section summary">

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
  <td><code>void</code></td>
  <td><pre><code>addMapIdleListener(MapIdleListener listener)</code></pre></td>
  <td><div class="block">
  Adds a listener for receiving idle state notifications and notifies it
  of the current state.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-style"
  title="class in com.here.sdk.mapview"><code>Style</code></a></td>
  <td><pre><code>getStyle()</code></pre></td>
  <td><div class="block">
  Gets the style that the map uses to customize the visual appearance of
  rendered features.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapIdleListener(MapIdleListener listener)</code></pre></td>
  <td><div class="block">
  Removes a listener from receiving idle state notifications.
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

  - <div id="addMapIdleListener(com.here.sdk.mapview.MapIdleListener)"
    class="section detail">

    ### addMapIdleListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapIdleListener</span><span class="parameters">(@NonNull
    [MapIdleListener](sdk-for-android-explore-com-here-sdk-mapview-mapidlelistener "interface in com.here.sdk.mapview") listener)</span>

    </div>

    <div class="block">

    Adds a listener for receiving idle state notifications and notifies
    it of the current state. The first notification received is always
    the state at the time of registration. The new listener is appended
    to the set of HereMap idle listeners as a strong reference. The
    caller is responsible for releasing the strong reference by calling
    removeMapIdleListener(com.here.sdk.mapview.MapIdleListener) .

    </div>

    Parameters:  
    `listener` -

    The listener

    </div>

  - <div id="removeMapIdleListener(com.here.sdk.mapview.MapIdleListener)"
    class="section detail">

    ### removeMapIdleListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapIdleListener</span><span class="parameters">(@NonNull
    [MapIdleListener](sdk-for-android-explore-com-here-sdk-mapview-mapidlelistener "interface in com.here.sdk.mapview") listener)</span>

    </div>

    <div class="block">

    Removes a listener from receiving idle state notifications.

    </div>

    Parameters:  
    `listener` -

    The listener

    </div>

  - <div id="getStyle()" class="section detail">

    ### getStyle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Style](sdk-for-android-explore-com-here-sdk-mapview-style "class in com.here.sdk.mapview")</span> <span class="element-name">getStyle</span>()

    </div>

    <div class="block">

    Gets the style that the map uses to customize the visual appearance
    of rendered features. Changes made to the map style using
    Style.update(com.here.sdk.mapview.Style) are lost when new scene is
    loaded using MapScene.loadScene(MapScheme,
    MapScene.LoadSceneCallback) and its variants as well as when map
    features are enabled or disabled using
    MapScene.enableFeatures(java.util.Map ) and
    MapScene.disableFeatures(java.util.List ) . Note: This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behavior. Related APIs may change for new releases without a
    deprecation process.

    </div>

    Returns:  
    The style that the map uses to customize the visual appearance of
    rendered features.

    </div>

  </div>

</div>


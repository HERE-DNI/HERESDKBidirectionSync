---
title: "EVSECapability (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-ev-evsecapability"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.ev](sdk-for-android-explore-com-here-sdk-ev-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
java.lang.Enum<EVSECapability>com.here.sdk.ev.EVSECapability →
java.lang.Enum → EVSECapability → com.here.sdk.ev.EVSECapability

</div>

<div id="class-description" class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`EVSECapability`](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum
</span><span class="element-name type-name-label">EVSECapability</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a><[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")></span>

</div>

<div class="block">

Represents the administrative functionality that an EVSE is capable of.
Note: This is a beta release of this feature, so there could be a few
bugs and unexpected behaviors. Related APIs may change for new releases
without a deprecation process.

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
  href="sdk-for-android-explore-com-here-sdk-ev-evsecapability#CHARGING_PREFERENCES"
  class="member-name-link"><code>CHARGING_PREFERENCES</code></a></td>
  <td><div class="block">
  The EVSE supports charging preferences.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evsecapability#CHARGING_PROFILE"
  class="member-name-link"><code>CHARGING_PROFILE</code></a></td>
  <td><div class="block">
  The EVSE supports charging profiles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evsecapability#REMOTE_START_STOP"
  class="member-name-link"><code>REMOTE_START_STOP</code></a></td>
  <td><div class="block">
  The EVSE can remotely be started/stopped.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evsecapability#RESERVABLE"
  class="member-name-link"><code>RESERVABLE</code></a></td>
  <td><div class="block">
  The EVSE can be reserved.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evsecapability#TOKEN_GROUP"
  class="member-name-link"><code>TOKEN_GROUP</code></a></td>
  <td><div class="block">
  This EVSE supports token groups, two or more tokens work as one, so that
  a session can be started with one token and stopped with another.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evsecapability#UNLOCK"
  class="member-name-link"><code>UNLOCK</code></a></td>
  <td><div class="block">
  Connectors have mechanical lock that can be requested by the eMSP to be
  unlocked.
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
  href="sdk-for-android-explore-com-here-sdk-ev-evsecapability"
  title="enum class in com.here.sdk.ev"><code>EVSECapability</code></a></td>
  <td><pre><code>valueOf(String name)</code></pre></td>
  <td><div class="block">
  Returns the enum constant of this class with the specified name.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-ev-evsecapability"
  title="enum class in com.here.sdk.ev"><code>EVSECapability</code></a><code>[]</code></td>
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

  - <div id="CHARGING_PROFILE" class="section detail">

    ### CHARGING_PROFILE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")</span> <span class="element-name">CHARGING_PROFILE</span>

    </div>

    <div class="block">

    The EVSE supports charging profiles.

    </div>

    </div>

  - <div id="CHARGING_PREFERENCES" class="section detail">

    ### CHARGING_PREFERENCES

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")</span> <span class="element-name">CHARGING_PREFERENCES</span>

    </div>

    <div class="block">

    The EVSE supports charging preferences.

    </div>

    </div>

  - <div id="REMOTE_START_STOP" class="section detail">

    ### REMOTE_START_STOP

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")</span> <span class="element-name">REMOTE_START_STOP</span>

    </div>

    <div class="block">

    The EVSE can remotely be started/stopped.

    </div>

    </div>

  - <div id="RESERVABLE" class="section detail">

    ### RESERVABLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")</span> <span class="element-name">RESERVABLE</span>

    </div>

    <div class="block">

    The EVSE can be reserved.

    </div>

    </div>

  - <div id="TOKEN_GROUP" class="section detail">

    ### TOKEN_GROUP

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")</span> <span class="element-name">TOKEN_GROUP</span>

    </div>

    <div class="block">

    This EVSE supports token groups, two or more tokens work as one, so
    that a session can be started with one token and stopped with
    another. This is handy when a card and key-fob are given to the
    EV-driver.

    </div>

    </div>

  - <div id="UNLOCK" class="section detail">

    ### UNLOCK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")</span> <span class="element-name">UNLOCK</span>

    </div>

    <div class="block">

    Connectors have mechanical lock that can be requested by the eMSP to
    be unlocked.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="values()" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")\[\]</span> <span class="element-name">values</span>()

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
    static</span> <span class="return-type">[EVSECapability](sdk-for-android-explore-com-here-sdk-ev-evsecapability "enum class in com.here.sdk.ev")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
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


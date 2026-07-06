---
title: "RoadShieldIconProperties (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.RoadShieldIconProperties

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RoadShieldIconProperties</span>
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Contains the information required to create a road shield image.

</div>

</div>

<div class="section summary">

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties#countryCode" class="member-name-link"><code>countryCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The country code in ISO-3166-1 alpha-3 format, which will determine
  the type of road shield.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties#routeNumberName" class="member-name-link"><code>routeNumberName</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A string that is used to additionally determine the road shield's
  visual representation.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`RouteType`](sdk-for-android-explore-com-here-sdk-core-routetype "enum class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties#routeType" class="member-name-link"><code>routeType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The type of route indicating the significance of the road in a range
  from 0 to 6.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties#shieldText" class="member-name-link"><code>shieldText</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The text of the road-shield.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties#stateCode" class="member-name-link"><code>stateCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The state code for the road.

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

      RoadShieldIconProperties(RouteType routeType,
       String countryCode,
       String stateCode,
       String routeNumberName,
       String shieldText)

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

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-routeType" class="section detail">

    ### routeType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RouteType](sdk-for-android-explore-com-here-sdk-core-routetype "enum class in com.here.sdk.core")</span> <span class="element-name">routeType</span>

    </div>

    <div class="block">

    The type of route indicating the significance of the road in a range
    from 0 to 6. A value of 1 stands for the most major route and 6 the
    most minor, with 0 being of unknown type.

    </div>

    </div>

  - <div id="sdk-for-android-explore-countryCode"
    class="section detail">

    ### countryCode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">countryCode</span>

    </div>

    <div class="block">

    The country code in ISO-3166-1 alpha-3 format, which will determine
    the type of road shield.

    </div>

    </div>

  - <div id="sdk-for-android-explore-stateCode" class="section detail">

    ### stateCode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">stateCode</span>

    </div>

    <div class="block">

    The state code for the road. It's a 2-letter code in ISO 3166-2
    format. For example the ones listed for US on this page
    https://en.wikipedia.org/wiki/ISO_3166-2:US. The code "AL" is for
    Alabama. Another example is the code for autonomous communities
    listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty
    if not required for the particular country.

    </div>

    </div>

  - <div id="sdk-for-android-explore-routeNumberName"
    class="section detail">

    ### routeNumberName

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">routeNumberName</span>

    </div>

    <div class="block">

    A string that is used to additionally determine the road shield's
    visual representation. In a routing context, the text can be taken
    from a LocalizedRoadNumber , which is available for each Span of a
    Route object. Typically, the string contains the number of a road,
    such as "E100". Internally, the text is parsed with a RegEx pattern
    and the results will be used along with other properties such as
    routeType , countryCode and stateCode to identify the visual
    representation of a road shield icon. Note that the actual text
    which will be displayed on the road shield icon is set with
    shieldText . In order to determine the visuals of the icon,
    countryCode , routeType and eventually the stateCode is in most
    cases sufficient to determine the type of road shield. In this case
    an empty string should be passed. Note: Texts that contain a
    CardinalDirection are currently not supported and may lead to
    unexpected results. See LocalizedRoadNumber for more details, it
    provides texts with and without a cardinal direction.

    </div>

    </div>

  - <div id="sdk-for-android-explore-shieldText" class="section detail">

    ### shieldText

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">shieldText</span>

    </div>

    <div class="block">

    The text of the road-shield. This is the text which is displayed on
    the road-shield in reality. It will be in the output road-shield
    icon.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.RouteType,java.lang.String,java.lang.String,java.lang.String,java.lang.String)"
    class="section detail">

    ### RoadShieldIconProperties

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoadShieldIconProperties</span><span class="parameters">(@NonNull
    [RouteType](sdk-for-android-explore-com-here-sdk-core-routetype "enum class in com.here.sdk.core") routeType,
    @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> countryCode,
    @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> stateCode,
    @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> routeNumberName,
    @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> shieldText)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `routeType` -

    The type of route indicating the significance of the road in a range
    from 0 to 6. A value of 1 stands for the most major route and 6 the
    most minor, with 0 being of unknown type.

    `countryCode` -

    The country code in ISO-3166-1 alpha-3 format, which will determine
    the type of road shield.

    `stateCode` -

    The state code for the road. It's a 2-letter code in ISO 3166-2
    format. For example the ones listed for US on this page
    https://en.wikipedia.org/wiki/ISO_3166-2:US. The code "AL" is for
    Alabama. Another example is the code for autonomous communities
    listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty
    if not required for the particular country.

    `routeNumberName` -

    A string that is used to additionally determine the road shield's
    visual representation. In a routing context, the text can be taken
    from a `LocalizedRoadNumber`, which is available for each `Span` of
    a `Route` object. Typically, the string contains the number of a
    road, such as "E100". Internally, the text is parsed with a RegEx
    pattern and the results will be used along with other properties
    such as `routeType, countryCode` and `stateCode` to identify the
    visual representation of a road shield icon. Note that the actual
    text which will be displayed on the road shield icon is set with
    [`shieldText`](sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties#shieldText).
    In order to determine the visuals of the icon, `countryCode, routeType` and eventually the `stateCode` is in most cases
    sufficient to determine the type of road shield. In this case an
    empty string should be passed. **Note:** Texts that contain a
    `CardinalDirection` are currently not supported and may lead to
    unexpected results. See `LocalizedRoadNumber` for more details, it
    provides texts with and without a cardinal direction.

    `shieldText` -

    The text of the road-shield. This is the text which is displayed on
    the road-shield in reality. It will be in the output road-shield
    icon.

    </div>

  </div>

</div>


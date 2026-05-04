---
title: "ManeuverAction (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaneuveraction"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class ManeuverAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.ManeuverAction
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`ManeuverAction`](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum ManeuverAction extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing")\>
Maneuver action type.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [ARRIVE](#ARRIVE)

Arrival maneuver, such as "You have reached your destination/waypoint".

[CONTINUE_ON](#CONTINUE_ON)

Continue maneuver, such as "Continue straight ahead".

[DEPART](#DEPART)

Departure maneuver, such as "Head towards".

[ENTER_HIGHWAY_FROM_LEFT](#ENTER_HIGHWAY_FROM_LEFT)

Merge onto a highway from the left side.

[ENTER_HIGHWAY_FROM_RIGHT](#ENTER_HIGHWAY_FROM_RIGHT)

Merge onto a highway from the right side.

[LEFT_EXIT](#LEFT_EXIT)

Left exit maneuver, such as "Take the exit".

[LEFT_FORK](#LEFT_FORK)

Left fork maneuver, such as "Keep left".

[LEFT_RAMP](#LEFT_RAMP)

Left ramp maneuver, such as "Join the highway".

[LEFT_ROUNDABOUT_ENTER](#LEFT_ROUNDABOUT_ENTER)

Roundabout maneuver (left-hand traffic), such as "Enter the roundabout".

[LEFT_ROUNDABOUT_EXIT1](#LEFT_ROUNDABOUT_EXIT1)

Roundabout maneuver (left-hand traffic), such as "Take the first exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT10](#LEFT_ROUNDABOUT_EXIT10)

Roundabout maneuver (left-hand traffic), such as "Take the tenth exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT11](#LEFT_ROUNDABOUT_EXIT11)

Roundabout maneuver (left-hand traffic), such as "Take the eleventh exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT12](#LEFT_ROUNDABOUT_EXIT12)

Roundabout maneuver (left-hand traffic), such as "Take the twelfth exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT2](#LEFT_ROUNDABOUT_EXIT2)

Roundabout maneuver (left-hand traffic), such as "Take the second exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT3](#LEFT_ROUNDABOUT_EXIT3)

Roundabout maneuver (left-hand traffic), such as "Take the third exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT4](#LEFT_ROUNDABOUT_EXIT4)

Roundabout maneuver (left-hand traffic), such as "Take the fourth exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT5](#LEFT_ROUNDABOUT_EXIT5)

Roundabout maneuver (left-hand traffic), such as "Take the fifth exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT6](#LEFT_ROUNDABOUT_EXIT6)

Roundabout maneuver (left-hand traffic), such as "Take the sixth exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT7](#LEFT_ROUNDABOUT_EXIT7)

Roundabout maneuver (left-hand traffic), such as "Take the seventh exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT8](#LEFT_ROUNDABOUT_EXIT8)

Roundabout maneuver (left-hand traffic), such as "Take the eighth exit at the roundabout".

[LEFT_ROUNDABOUT_EXIT9](#LEFT_ROUNDABOUT_EXIT9)

Roundabout maneuver (left-hand traffic), such as "Take the ninth exit at the roundabout".

[LEFT_ROUNDABOUT_PASS](#LEFT_ROUNDABOUT_PASS)

Roundabout maneuver (left-hand traffic), such as "Pass the roundabout".

[LEFT_TURN](#LEFT_TURN)

Left turn maneuver, such as "Turn left".

[LEFT_U_TURN](#LEFT_U_TURN)

Left-hand U-turn maneuver, such as "Make a U-turn".

[MIDDLE_FORK](#MIDDLE_FORK)

Middle fork maneuver, such as "Keep middle".

[RIGHT_EXIT](#RIGHT_EXIT)

Right exit maneuver, such as "Take the exit".

[RIGHT_FORK](#RIGHT_FORK)

Right fork maneuver, such as "Keep right".

[RIGHT_RAMP](#RIGHT_RAMP)

Right ramp maneuver, such as "Join the highway".

[RIGHT_ROUNDABOUT_ENTER](#RIGHT_ROUNDABOUT_ENTER)

Roundabout maneuver (right-hand traffic), such as "Enter the roundabout".

[RIGHT_ROUNDABOUT_EXIT1](#RIGHT_ROUNDABOUT_EXIT1)

Roundabout maneuver (right-hand traffic), such as "Take the first exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT10](#RIGHT_ROUNDABOUT_EXIT10)

Roundabout maneuver (right-hand traffic), such as "Take the tenth exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT11](#RIGHT_ROUNDABOUT_EXIT11)

Roundabout maneuver (right-hand traffic), such as "Take the eleventh exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT12](#RIGHT_ROUNDABOUT_EXIT12)

Roundabout maneuver (right-hand traffic), such as "Take the twelfth exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT2](#RIGHT_ROUNDABOUT_EXIT2)

Roundabout maneuver (right-hand traffic), such as "Take the second exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT3](#RIGHT_ROUNDABOUT_EXIT3)

Roundabout maneuver (right-hand traffic), such as "Take the third exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT4](#RIGHT_ROUNDABOUT_EXIT4)

Roundabout maneuver (right-hand traffic), such as "Take the fourth exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT5](#RIGHT_ROUNDABOUT_EXIT5)

Roundabout maneuver (right-hand traffic), such as "Take the fifth exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT6](#RIGHT_ROUNDABOUT_EXIT6)

Roundabout maneuver (right-hand traffic), such as "Take the sixth exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT7](#RIGHT_ROUNDABOUT_EXIT7)

Roundabout maneuver (right-hand traffic), such as "Take the seventh exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT8](#RIGHT_ROUNDABOUT_EXIT8)

Roundabout maneuver (right-hand traffic), such as "Take the eighth exit at the roundabout".

[RIGHT_ROUNDABOUT_EXIT9](#RIGHT_ROUNDABOUT_EXIT9)

Roundabout maneuver (right-hand traffic), such as "Take the ninth exit at the roundabout".

[RIGHT_ROUNDABOUT_PASS](#RIGHT_ROUNDABOUT_PASS)

Roundabout maneuver (right-hand traffic), such as "Pass the roundabout".

[RIGHT_TURN](#RIGHT_TURN)

Right turn maneuver, such as "Turn right".

[RIGHT_U_TURN](#RIGHT_U_TURN)

Right u-turn maneuver, such as "Make a U-turn".

[SHARP_LEFT_TURN](#SHARP_LEFT_TURN)

Sharp left turn maneuver, such as "Turn sharply left".

[SHARP_RIGHT_TURN](#SHARP_RIGHT_TURN)

Sharp right turn maneuver, such as "Turn sharply right".

[SLIGHT_LEFT_TURN](#SLIGHT_LEFT_TURN)

Slight left turn maneuver, such as "Turn slightly left".

[SLIGHT_RIGHT_TURN](#SLIGHT_RIGHT_TURN)

Slight right turn maneuver, such as "Turn slightly right".

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`ManeuverAction`](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`ManeuverAction`](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### DEPART

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") DEPART

    Departure maneuver, such as "Head towards".

### ARRIVE

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") ARRIVE

    Arrival maneuver, such as "You have reached your destination/waypoint".

### LEFT_U_TURN

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_U_TURN

    Left-hand U-turn maneuver, such as "Make a U-turn".

### SHARP_LEFT_TURN

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") SHARP_LEFT_TURN

    Sharp left turn maneuver, such as "Turn sharply left".

### LEFT_TURN

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_TURN

    Left turn maneuver, such as "Turn left".

### SLIGHT_LEFT_TURN

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") SLIGHT_LEFT_TURN

    Slight left turn maneuver, such as "Turn slightly left".

### CONTINUE_ON

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") CONTINUE_ON

    Continue maneuver, such as "Continue straight ahead".

### SLIGHT_RIGHT_TURN

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") SLIGHT_RIGHT_TURN

    Slight right turn maneuver, such as "Turn slightly right".

### RIGHT_TURN

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_TURN

    Right turn maneuver, such as "Turn right".

### SHARP_RIGHT_TURN

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") SHARP_RIGHT_TURN

    Sharp right turn maneuver, such as "Turn sharply right".

### RIGHT_U_TURN

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_U_TURN

    Right u-turn maneuver, such as "Make a U-turn".

### LEFT_EXIT

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_EXIT

    Left exit maneuver, such as "Take the exit".

### RIGHT_EXIT

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_EXIT

    Right exit maneuver, such as "Take the exit".

### LEFT_RAMP

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_RAMP

    Left ramp maneuver, such as "Join the highway".

### RIGHT_RAMP

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_RAMP

    Right ramp maneuver, such as "Join the highway".

### LEFT_FORK

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_FORK

    Left fork maneuver, such as "Keep left".

### MIDDLE_FORK

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") MIDDLE_FORK

    Middle fork maneuver, such as "Keep middle".

### RIGHT_FORK

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_FORK

    Right fork maneuver, such as "Keep right".

### ENTER_HIGHWAY_FROM_LEFT

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") ENTER_HIGHWAY_FROM_LEFT

    Merge onto a highway from the left side. Such a maneuver occurs only in countries that drive on the left side of the road (left-hand traffic).

    **Note:** This action is only generated when using the Navigate license. On top, until release of HERE SDK 4.16.0, it needs to be enabled via `RouteOptions`.

### ENTER_HIGHWAY_FROM_RIGHT

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") ENTER_HIGHWAY_FROM_RIGHT

    Merge onto a highway from the right side. Such a maneuver occurs only in countries that drive on the right side of the road (right-hand traffic).

    **Note:** This action is only generated when using the Navigate license. On top, until release of HERE SDK 4.16.0, it needs to be enabled via `RouteOptions`.

### LEFT_ROUNDABOUT_ENTER

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_ENTER

    Roundabout maneuver (left-hand traffic), such as "Enter the roundabout".

### RIGHT_ROUNDABOUT_ENTER

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_ENTER

    Roundabout maneuver (right-hand traffic), such as "Enter the roundabout".

### LEFT_ROUNDABOUT_PASS

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_PASS

    Roundabout maneuver (left-hand traffic), such as "Pass the roundabout".

### RIGHT_ROUNDABOUT_PASS

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_PASS

    Roundabout maneuver (right-hand traffic), such as "Pass the roundabout".

### LEFT_ROUNDABOUT_EXIT1

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT1

    Roundabout maneuver (left-hand traffic), such as "Take the first exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT2

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT2

    Roundabout maneuver (left-hand traffic), such as "Take the second exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT3

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT3

    Roundabout maneuver (left-hand traffic), such as "Take the third exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT4

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT4

    Roundabout maneuver (left-hand traffic), such as "Take the fourth exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT5

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT5

    Roundabout maneuver (left-hand traffic), such as "Take the fifth exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT6

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT6

    Roundabout maneuver (left-hand traffic), such as "Take the sixth exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT7

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT7

    Roundabout maneuver (left-hand traffic), such as "Take the seventh exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT8

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT8

    Roundabout maneuver (left-hand traffic), such as "Take the eighth exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT9

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT9

    Roundabout maneuver (left-hand traffic), such as "Take the ninth exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT10

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT10

    Roundabout maneuver (left-hand traffic), such as "Take the tenth exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT11

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT11

    Roundabout maneuver (left-hand traffic), such as "Take the eleventh exit at the roundabout".

### LEFT_ROUNDABOUT_EXIT12

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") LEFT_ROUNDABOUT_EXIT12

    Roundabout maneuver (left-hand traffic), such as "Take the twelfth exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT1

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT1

    Roundabout maneuver (right-hand traffic), such as "Take the first exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT2

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT2

    Roundabout maneuver (right-hand traffic), such as "Take the second exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT3

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT3

    Roundabout maneuver (right-hand traffic), such as "Take the third exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT4

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT4

    Roundabout maneuver (right-hand traffic), such as "Take the fourth exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT5

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT5

    Roundabout maneuver (right-hand traffic), such as "Take the fifth exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT6

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT6

    Roundabout maneuver (right-hand traffic), such as "Take the sixth exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT7

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT7

    Roundabout maneuver (right-hand traffic), such as "Take the seventh exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT8

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT8

    Roundabout maneuver (right-hand traffic), such as "Take the eighth exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT9

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT9

    Roundabout maneuver (right-hand traffic), such as "Take the ninth exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT10

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT10

    Roundabout maneuver (right-hand traffic), such as "Take the tenth exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT11

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT11

    Roundabout maneuver (right-hand traffic), such as "Take the eleventh exit at the roundabout".

### RIGHT_ROUNDABOUT_EXIT12

public static final [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") RIGHT_ROUNDABOUT_EXIT12

    Roundabout maneuver (right-hand traffic), such as "Take the twelfth exit at the roundabout".

## Method Details

### values

public static [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null

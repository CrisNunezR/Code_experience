-- Keep a log of any SQL queries you execute as you solve the mystery.

--1) Search the crime_scene_reports table to identify the crime's report amongst those of the
--same day and place
SELECT description FROM crime_scene_reports
    WHERE street LIKE "%Humphrey%" AND day == 28 AND month == 07;
    --Findings:
        --time of theft: 10.15am
        --place: Humphrey Street Bakery
        --3 witnesses that were interviewed (all were present at the time)
            --their interviews transcripts mention the "bakery"!
        --littering took place at 16:36, no known witnesses

--2) Search the transcripts on the interviews table looking for 'bakery' on the transcript
SELECT transcript, name FROM interviews
    WHERE transcript like '%bakery%'
    AND year == 2021 AND month == 7 AND day == 28
    --Findinds:
        --Ruth: 10min after the theft, the thief got into a car (look at security footage from bakery
            --parking lot)
        --Eugene: Saw the thief withdrawing money at the ATM on Leggett Street early that morning
        --Raymond: thief called an accomplice for less than a minute when leaving the bakery and
            --asked him/her to buy a flight ticket for the earliest flight the day after

--3) Look at ATM
SELECT people.passport_number, atm.account_number, transaction_type, atm.amount, people.name
    FROM atm_transactions AS atm
    JOIN bank_accounts AS bank ON atm.account_number == bank.account_number
    JOIN people ON people.id == bank.person_id
    WHERE atm_location LIKE "%Leggett Street%" AND transaction_type == 'withdraw'
    AND atm.day == 28 AND atm.month == 07 AND atm.year == 2021
    --Findings:
        --8 ppl made withdrawals: Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, Benista
        --(no time register, so we can't know which transactions were made in the morning)
        --account numbers:
            --28500762
            --28296815
            --76054385
            --49610011
            --16153065
            --25506511
            --81061156
            --26013199

--4) Look at bakery security footage around 10.25am
SELECT b_log.license_plate, activity, hour, minute, people.name
    FROM bakery_security_logs as b_log
    JOIN people ON people.license_plate == b_log.license_plate
    WHERE day == 28 AND month == 07 AND year == 2021
    AND hour ==10 AND minute > 15 AND minute < 35
    AND activity == 'exit'
    --Findings:
        --8 cars leaving the parking lot between 10.15am and 10.35am

        --combining the 2 informations:
        SELECT people.passport_number, atm.account_number, transaction_type, atm.amount, people.name
            FROM atm_transactions AS atm
            JOIN bank_accounts AS bank ON atm.account_number == bank.account_number
            JOIN people ON people.id == bank.person_id
            WHERE atm_location LIKE "%Leggett Street%" AND transaction_type == 'withdraw'
            AND atm.day == 28 AND atm.month == 07 AND atm.year == 2021
            AND people.license_plate IN (
                SELECT b_log.license_plate
                    FROM bakery_security_logs as b_log
                    JOIN people ON people.license_plate == b_log.license_plate
                    WHERE day == 28 AND month == 07 AND year == 2021
                    AND hour ==10 AND minute > 15 AND minute < 35
                    AND activity == 'exit')
        --with this we can narrow the suspects to 4: Bruce (10:18am), Diana (10:23am), Iman (10:21am) and Luca (10:19am)

--5) Call Log: numbers that made calls with duration less than a minute on the day of the theft
SELECT caller, receiver, duration, call.name, receiv.name
    FROM phone_calls
    JOIN people as call ON call.phone_number == phone_calls.caller
    JOIN people as receiv ON receiv.phone_number == phone_calls.receiver
    WHERE year == 2021 AND month == 07 AND day == 28 AND duration < 60

        --combining the 3:
        SELECT DISTINCT people.passport_number, atm.account_number, transaction_type, phone_calls.caller,
            phone_calls.duration, people.name
        FROM atm_transactions AS atm
        JOIN bank_accounts AS bank ON atm.account_number == bank.account_number
        JOIN people ON people.id == bank.person_id
        JOIN phone_calls ON phone_calls.caller == people.phone_number
        WHERE atm_location LIKE "%Leggett Street%" AND transaction_type == 'withdraw'
        AND atm.day == 28 AND atm.month == 07 AND atm.year == 2021
        AND people.license_plate IN (
            SELECT b_log.license_plate
                FROM bakery_security_logs as b_log
                JOIN people ON people.license_plate == b_log.license_plate
                WHERE day == 28 AND month == 07 AND year == 2021
                AND hour ==10 AND minute > 15 AND minute < 35
                AND activity == 'exit')
        AND phone_calls.caller IN (
            SELECT caller
                FROM phone_calls
                JOIN people ON people.phone_number == phone_calls.caller
                WHERE year == 2021 AND month == 07 AND day == 28 AND duration < 60)
        AND phone_calls.month == 07 AND phone_calls.day == 28 AND phone_calls.duration < 60
        --Narrow down to 2 suspects: Bruce (call 45s) and Diana (call 49s)


--6) We also know the thief might have taken a flight the following day in the morning
--so we can look at the flights that morning and their passengers
SELECT origin_airport_id, full_name, destination_airport_id, hour, passport_number, seat
    FROM flights
    INNER JOIN passengers ON flights.id == passengers.flight_id
    INNER JOIN airports ON airports.id == flights.origin_airport_id
    WHERE year == 2021 AND month == 07 AND day == 29

        --combining all information:
        SELECT DISTINCT passengers.passport_number, atm.account_number, transaction_type, phone_calls.caller,
            phone_calls.duration, airports.full_name, people.name
        FROM atm_transactions AS atm
        JOIN bakery_security_logs AS log ON log.license_plate == people.license_plate
        JOIN bank_accounts AS bank ON atm.account_number == bank.account_number
        JOIN people ON people.id == bank.person_id
        JOIN phone_calls ON phone_calls.caller == people.phone_number
        JOIN passengers ON passengers.passport_number == people.passport_number
        JOIN flights ON flights.id == passengers.flight_id
        JOIN airports ON flights.destination_airport_id == airports.id
        WHERE atm_location LIKE "%Leggett Street%" AND transaction_type == 'withdraw'
        AND atm.day == 28 AND atm.month == 07 AND atm.year == 2021
        AND people.license_plate IN (
            SELECT b_log.license_plate
                FROM bakery_security_logs as b_log
                JOIN people ON people.license_plate == b_log.license_plate
                WHERE day == 28 AND month == 07 AND year == 2021
                AND hour ==10 AND minute > 15 AND minute < 35
                AND activity == 'exit')
            AND log.day == 28 AND log.month == 7
        AND phone_calls.caller IN (
            SELECT caller
                FROM phone_calls
                JOIN people ON people.phone_number == phone_calls.caller
                WHERE year == 2021 AND month == 07 AND day == 28 AND duration < 60)
            AND phone_calls.month == 07 AND phone_calls.day == 28 AND phone_calls.duration < 60
        AND flights.year == 2021 AND flights.month == 7 AND flights.day == 29 AND flights.hour < 12

        --since we know the thief meant to leave during the morning, we can narrow down the suspect list to just Bruce!
        --who we know departed towards LaGuardia, New York

--7) From the call logs on query 5 we know Bruce called Robin, his accomplice!
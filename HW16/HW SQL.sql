--select * from Users
-- select * from Host
--select * from Reservation
--select * from Guest
--select * from Room
--select * from Review
--SELECT hostID FROM Host WHERE hostID IN (7, 8, 9);


--INSERT INTO Guest (usersID)
--VALUES (1), (4), (5);

--add hostid
--INSERT INTO Room (price, AC, refrigerator)
--VALUES (100.0, true, true),
--       (120.0, true, false),
--       (80.0, false, true);
--
--INSERT INTO Room(hostID)
--VALUES (7), (8), (9)

--add reservationid and hostid
--INSERT INTO Host (usersID, reservationID, host_rating, host_description)
--VALUES (1, 1, 4.5, 'Experienced host'),
--       (2, 2, 4.2, 'Friendly and helpful'),
--       (3, 3, 4.8, 'Great hospitality');

--INSERT INTO Host(usersid)
--VALUES (1), (4), (5)

--
--INSERT INTO Reservation (guestID, roomID, check_in, check_out, total_price)
--VALUES (10, 19, '2023-08-01', '2023-08-05', 400.0),
--       (11, 20, '2023-08-10', '2023-08-15', 600.0),
--       (12, 21, '2023-08-05', '2023-08-08', 240.0);

--
--INSERT INTO Review (guestID, hostID, reservationID, rating, review_text, review_date)
--VALUES (10, 7, 13, 4.7, 'Had a wonderful stay!', '2023-08-06'),
--       (11, 8, 14, 4.0, 'Nice place, but noisy neighbors', '2023-08-16'),
--       (12, 9, 15, 5.0, 'Outstanding experience', '2023-08-09');



--The biggest amount of revervations
--SELECT u.name AS username, u.usersID AS user_id
--FROM Users u
--JOIN Guest g ON u.usersID = g.usersID
--JOIN Reservation r ON g.guestID = r.guestID
--GROUP BY u.usersID
--ORDER BY COUNT(r.reservationID) DESC
--LIMIT 1;


-- The biggest host rate
--SELECT h.hostID AS host_id, h.host_description AS hostname
--FROM Host h
--JOIN Review rev ON h.hostID = rev.hostID
--GROUP BY h.hostID, h.host_description
--ORDER BY AVG(rev.rating) DESC
--LIMIT 1;


--
--SELECT u.name AS username, u.usersID AS user_id
--FROM Users u
--JOIN Guest g ON u.usersID = g.usersID
--JOIN Reservation r ON g.guestID = r.guestID
--GROUP BY u.usersID, u.name
--ORDER BY COUNT(r.reservationID) DESC
--LIMIT 1;


--SELECT h.hostID AS host_id, h.host_description AS hostname
--FROM Host h
--JOIN Room r ON h.hostID = r.hostID
--JOIN Reservation res ON r.roomID = res.roomID
--WHERE res.check_in BETWEEN DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month') 
--                       AND DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 day'
--GROUP BY h.hostID, h.host_description
--ORDER BY SUM(res.total_price) DESC
--LIMIT 1;


-- SELECT h.hostID AS host_id, h.host_description AS hostname
-- FROM Host h
-- JOIN Review rev ON h.hostID = rev.hostID
-- GROUP BY h.hostID, h.host_description
-- ORDER BY AVG(rev.rating) DESC
-- LIMIT 1;



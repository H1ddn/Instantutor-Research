function out = cbModel(user, db)

    % test code
    %user = [1, 0, 1, 1, 0, 1, 1, 0, 0, 1];
    %N = 10;
    %db = transpose(dec2bin(0:2^N-1)' - '0');
    
    % t is the number of tutors
    t = size(db,1);
    % v is the number of variables
    % user variable count and db variable count must be the same
    v = size(db,2);
    sorted = zeros(t,2);

    % test code
    %for i = 1:t
    %    db(i,1) = i;
    %end


    for i = 1:t
        % tot = number of similarities between the user 
        % and specific tutor #i
        tot = 0;
        % j starts as 2 since j's first value will be userID
        for j = 2:v
            % if variable #j in user and tutor is equal
            % increment tot
            if(user(j) == db(i,j))
                tot = tot + 1;
            end
        end
        tot = tot/(v-1);
        % first column is tutor's similarity score to user
        % next column is tutor's userID
        sorted(i,1) = tot;
        sorted(i,2) = db(i,1);
    end

    sorted = flip(sortrows(sorted), 1);

    if(t < 10)
        out = sorted(1:t,:);
    else
        out = sorted(1:10,:);
    end